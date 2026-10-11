#!/usr/bin/env python3
"""Complete source-pinned non-hosting PR443 target-mixing replay.
Prepared for eumemic with OpenAI Codex assistance; Apache-2.0.
"""
import argparse, gzip, hashlib, io, json, os, shutil, subprocess, sys, time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('output',type=Path);a=ap.parse_args()
 out=a.output.resolve();assert not out.is_relative_to(HERE),'output must be outside the package'
 assert not out.exists(),'use a fresh output directory';out.mkdir(parents=True)
 assert sys.flags.optimize==0,'assertions must remain enabled'
 manifest_sha=digest(HERE/'MANIFEST.json')
 manifest=json.loads((HERE/'MANIFEST.json').read_text())
 actual={p.relative_to(HERE).as_posix():digest(p) for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=HERE/'MANIFEST.json'}
 assert actual==manifest,'package manifest mismatch'
 sources=json.loads((HERE/'SOURCES.json').read_text());count=0
 for entry in sources.values():
  for rel,sha in entry['files'].items():
   data=(HERE/rel).read_bytes();assert hashlib.sha1(b'blob %d\0'%len(data)+data).hexdigest()==sha,rel;count+=1
 expected=json.loads((HERE/'EXPECTED.json').read_text());parent=HERE/'e8-r740-replica32';word=HERE/'data/word.json'
 assert hashlib.sha256(word.read_bytes()).hexdigest()==expected['content_sha256']
 env=dict(os.environ,PYTHON=sys.executable,PYTHONDONTWRITEBYTECODE='1');env.pop('PYTHONOPTIMIZE',None)
 steps=[]
 def run(name,argv):
  start=time.monotonic()
  with (out/(name+'.log')).open('w') as f:p=subprocess.run(list(map(str,argv)),cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT)
  steps.append(dict(name=name,exit_code=p.returncode,seconds=time.monotonic()-start))
  write(out/'STEPS.json',steps)
  if p.returncode:
   print((out/(name+'.log')).read_text()[-8000:],flush=True)
   write(out/'FAILURE.json',dict(step=name,exit_code=p.returncode));raise RuntimeError(name)
  print('PASS',name,flush=True)
 def py(name,file,*args):run(name,[sys.executable,'-B',file,*args])
 run('parent443-full',['bash',parent/'verify.sh',out/'parent443'])
 py('mix-generate',HERE/'vendor450/code/mix_target.py',parent/'data/word.json.gz',out/'regenerated-word.json')
 assert (out/'regenerated-word.json').read_bytes()==word.read_bytes(),'regenerated mixed word differs'
 old=json.loads(gzip.decompress((parent/'data/word.json.gz').read_bytes()));new=json.loads(word.read_bytes())
 for key in ['R','v','h','lines','frames','start','final','A','C','ret']:
  assert new[key]==old[key],('unexpected change',key)
 assert len(new['target_mix']['receivers'])==46
 B=parent/'parent436/code/bit';bin=out/'parent443/parent/bin';candidate=out/'candidate';nine=candidate/'nine';nine.mkdir(parents=True)
 py('export',B/'export_records.py',word,candidate/'records')
 py('mix-check',HERE/'vendor450/code/mix_check.py',word,candidate/'records','--controls',parent/'data/word.json.gz')
 py('cohort',B/'regression/stage_cohort.py',candidate/'records',candidate/'records',candidate/'cin',candidate/'cout')
 run('legality',[bin/'legality',candidate/'cin',candidate/'cout',candidate/'cout/legality.json'])
 run('columns-five',[bin/'columns_h',candidate/'cout/COHORT249-RECORDS.bin',candidate/'cout/columns.json'])
 run('columns-nine',[bin/'columns_k4',candidate/'cout/COHORT249-RECORDS.bin',candidate/'cout/columns_k4.json'])
 py('record-mutations',B/'mutate_records.py',candidate/'records',candidate/'cin',candidate/'cout',bin/'legality',bin/'columns_k4',bin/'legality_ncopy_h')
 py('gram',B/'checkers/gram_frames.py',candidate/'records','--gram','e8ham','--h','8','--positive')
 shutil.copyfile(out/'parent443/candidate/nine/GEOMETRY.json',nine/'GEOMETRY.json')
 # Runtime is deliberately excluded from the geometry witness hash so the
 # source-bound template is reproducible across hosts and Python versions.
 geometry=json.loads((nine/'GEOMETRY.json').read_text()); geometry['seconds']=0; write(nine/'GEOMETRY.json',geometry)
 runtime_word=out/'mixed-runtime.json.gz'; buf=io.BytesIO(); z=gzip.GzipFile(fileobj=buf,mode='wb',filename='',mtime=0); z.write(word.read_bytes()); z.close(); runtime_word.write_bytes(buf.getvalue())
 py('global',parent/'code/global_kernel.py','--word',runtime_word,'--local-check',candidate,'--out',nine,'--isometries',parent/'data/residual-isometries.json')
 py('audit',parent/'code/audit_kernel.py','--word',runtime_word,'--local-check',candidate,'--out',nine)
 py('compose',parent/'code/compose_kernel.py','--pricing',parent/'parent436/code/pricing','--out',nine,'--cited',parent/'parent436/data/complex-b-433.json','--receipt',parent/'parent436/data/controls/pr433/CERTIFICATE.json')
 # The independent exact frame/operator audit discharges the changed target-read interface.
 py('operator-audit',HERE/'code/operator_audit.py','--word',word,'--parent',parent/'data/word.json.gz','--out',out/'OPERATOR-AUDIT.json')
 g=json.loads((nine/'GLOBAL.json').read_text());r=json.loads((nine/'COMPOSED-433.json').read_text())
 for key,value in expected['global'].items():assert g[key]==value,(key,g[key],value)
 for key,value in expected['result'].items():assert r[key]==value,(key,r[key],value)
 assert len(r['strict_outer_constraints'])==47 and len(r['outer_controls'])==4
 assert digest(HERE/'MANIFEST.json')==manifest_sha,'manifest changed during replay'
 after={p.relative_to(HERE).as_posix():digest(p) for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=HERE/'MANIFEST.json'}
 assert after==manifest,'source changed during replay'
 write(out/'RESULT.json',dict(status='PASS_NONHOSTING_TARGET_MIXING',kappa=r['kappa'],bit_lower=r['bit_lower'],complex_lower=r['complex_lower'],content_sha256=expected['content_sha256'],template_sha256=g['template_sha256'],operator_audit_sha256=digest(out/'OPERATOR-AUDIT.json'),package_manifest_sha256=manifest_sha,source_blobs_checked=count,steps=steps,python=sys.version))
 print('PASS conditional kappa',r['kappa'],'=',r['kappa_decimal'],flush=True)
if __name__=='__main__':main()
