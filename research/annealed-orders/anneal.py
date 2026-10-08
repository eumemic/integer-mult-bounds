#!/usr/bin/env python3
"""Simulated annealing on the role count R = c + q - matched (not part of make verify).

State: PR #47 adjacent-swap bits plus one point order per common point. Moves flip
1-4 bits, swap two points, swap two consecutive pairs, or swap a pair's members in
one group's order. R comes from PR #47's profiler stopped before the block profile
(max-cardinality matching). Usage: anneal.py H SEED SECONDS OUT.json [START.json]
"""
import json, math, os, random, shlex, subprocess, sys, tempfile, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'scripts')); sys.path.insert(0, str(HERE))
from partial_swap.graph import export
from annealed_graph import graph, pinned

def counter(work):
    src = (ROOT/'research/climbed-producers/profiles.cpp').read_text()
    mark = '// Reconstruct the actual transition multiset'
    (work/'rcount.cpp').write_text(src.replace(mark, 'if(getenv("R_ONLY"))return 0;\n'+mark, 1))
    subprocess.run([*shlex.split(os.environ.get('CXX', 'c++')), '-O3', '-std=c++17', '-include', 'algorithm',
                    '-I', str(ROOT/'scripts/partial_swap'), str(work/'rcount.cpp'), '-o', str(work/'rcount')], check=True)
    return work/'rcount'

def roles(exe, work, h, bits, orders):
    dag = work/f'h{h}.bin'; export(graph(h, bits, orders), dag)
    out = subprocess.run([str(exe), str(dag)], capture_output=True, text=True, env=dict(os.environ, R_ONLY='1'))
    return json.loads(out.stdout.splitlines()[0])['R']

def main(h, seed, secs, out, start=None):
    rng = random.Random(seed); work = Path(tempfile.mkdtemp(prefix='anneal-')); exe = counter(work)
    if start:
        d = json.loads(Path(start).read_text()); bits, orders = d['bits'], d['orders']
    else:
        bits, orders = pinned(h)
    cur = best = roles(exe, work, h, bits, orders); keep = (bits, orders); t0 = time.time()
    T0 = float(os.environ.get('T0', '0.6'))
    while time.time()-t0 < secs:
        nb, no = bits[:], [o[:] for o in orders]
        if rng.random() < 0.5:
            for _ in range(rng.choice([1, 1, 2, 3, 4])):
                nb[rng.randrange(len(nb))] ^= 1
        else:
            o = no[rng.randrange(h)]; t = rng.random()
            if t < 0.4:
                x, y = rng.sample(range(len(o)), 2); o[x], o[y] = o[y], o[x]
            elif t < 0.7:
                x, y = rng.sample(range(len(o)//2), 2); o[2*x:2*x+2], o[2*y:2*y+2] = o[2*y:2*y+2], o[2*x:2*x+2]
            else:
                x = rng.randrange(len(o)//2); o[2*x], o[2*x+1] = o[2*x+1], o[2*x]
        try:
            val = roles(exe, work, h, nb, no)
        except Exception:
            continue
        T = T0*(1-(time.time()-t0)/secs)+1e-9
        if val <= cur or rng.random() < math.exp(-(val-cur)/T):
            bits, orders, cur = nb, no, val
            if val < best:
                best, keep = val, (nb, no)
                Path(out).write_text(json.dumps(dict(h=h, R=best, bits=nb, orders=no)))
    Path(out).write_text(json.dumps(dict(h=h, R=best, bits=keep[0], orders=keep[1])))
    print(f'h={h} seed={seed} best R={best}')

if __name__ == '__main__':
    a = sys.argv[1:]
    main(int(a[0]), int(a[1]), float(a[2]), a[3], a[4] if len(a) > 4 else None)
