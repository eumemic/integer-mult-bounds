"""Pinned PR117 scalar DAG adapter for the saturated deferred compiler.

The searched graph is upstream PR117 work credited to eumemic with Anthropic
Claude assistance. This adapter preserves that witness and producer unchanged;
saturation integration is separate OpenAI Codex-assisted work. Apache-2.0.
"""
from hashlib import sha256
from pathlib import Path
from replayed_producer import build as replayed_build

WITNESS_SHA256 = 'b95a7bf02b483c6cb2a65d3302c5757d93801d24f8fb33f694093736aad9f884'

def build(h, prefix, central_disjoint, base=2):
    assert central_disjoint == h and base == 2
    witness=Path(__file__).resolve().parent/'inputs/complex-dag.json.gz'
    assert sha256(witness.read_bytes()).hexdigest() == WITNESS_SHA256, 'PR117 DAG pin mismatch'
    result = replayed_build(witness,prefix)
    assert result['h'] == h, 'row and witness dimensions differ'
    return result
