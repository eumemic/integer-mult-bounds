"""PR #47 producers with annealed per-group point orders and summand orders.

Same circuit as research/climbed-producers/climbed_graph.py (RaD/hipotures
PR #41 producer, Rohan Arun's PR #47 adjacent-swap bits), except that each
common point uses its own pinned point order (orders-{h}.json) instead of
RaD's alternating order. Found by simulated annealing on the role count R.
Prepared by eumemic with Anthropic Claude assistance. Apache-2.0.
"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from partial_swap.paired import PairedExclusionCircuit
from partial_swap.shared import SharedPointCircuit


def pinned(h):
    d = json.loads((HERE/f'orders-{h}.json').read_text())
    assert d['h'] == h and all(b in (0, 1) for b in d['bits'])
    assert len(d['orders']) == h
    for i, order in enumerate(d['orders']):
        assert sorted(order) == [x for x in range(h) if x != i], 'Point order must list every other point once'
    return d['bits'], d['orders']


def graph(h, bits=None, orders=None):
    assert h in (23, 25)
    if bits is None or orders is None:
        bits, orders = pinned(h)
    pos = [0]
    class Changed(PairedExclusionCircuit):
        base_threshold = 2
        def total(self, values):
            values = [x for x in values if x]
            values.sort(key=lambda node: (self.support[node].bit_count(), self.support[node]), reverse=True)
            for i in range(len(values)-1):
                k = pos[0]; pos[0] += 1
                if k < len(bits) and bits[k]:
                    values[i], values[i+1] = values[i+1], values[i]
            result = 0
            for node in values:
                result = self.add(result, node)
            return result
    local = Changed(h-1)
    total = local.pair(list(range(h-1)))[0]
    local.outputs[()] = total
    stack = [total]
    while stack:
        node = stack.pop()
        if not node or node in local.active:
            continue
        local.active.add(node)
        if local.args[node]:
            stack.extend(local.args[node])
    local.additions = sum(local.args[node] is not None for node in local.active)
    assert pos[0] == len(bits), 'Swap decision count mismatch'
    return SharedPointCircuit(h, local, point_order=lambda _, i: orders[i])
