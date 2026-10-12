# Independent replay of PR592

**Conditional κ = 0.001612719427075359** (conservative value
`0.001612719424224312`). This is an independent clean replay of
[CrocSwap/integer-mult-bounds#592](https://github.com/CrocSwap/integer-mult-bounds/pull/592),
head `9092320f7932dbe61a78f15b6c5fd6a0cbd41307`.

The replay rebuilt the frozen PR558 baseline and both final provider words
from the pinned PR568/569/571/575/583 source packages. It completed 32
top-level stages plus the nine nested baseline stages in 338.45477745798416
seconds, from a fresh baseline with no reused local or baseline outputs. The
result is `PASS_HPEQ4_NATIVE_COMPLEX_AND_CITED_BIT`.

The replay checked the actual scalar words, arbitrary dirty restoration, both
reflected ledgers, phase edges, normalized wrappers, physical owner/profile
data, a fresh invoice, exact assembly, two exact moment engines, 47 outer
constraints, 147 assembly controls, timing controls, and recompression/rebound
controls. The resulting profile is
`{1:182818,2:34193,3:22560,4:14584,5:4032,6:4032,8:576,12:1,48:1969}`
with dispatch `ck=53`, `atm3=19`.

PR592 changes only the owner dispatch from PR591: the hyperplane-ended helper
chain is retained, with 38 width-8 helpers per call ending on the certified
terminal hyperplane and becoming width 7. The changed literal owner map is
mass-neutral and leaves the rank deficit unchanged while improving the paid
profile. The independent replay's receipt SHA256 is
`13db1006088ecb880815fb116e6cc464b2e18c91426bdf3a9efdad481427beae`; its
result SHA256 is
`f36956b317d8dddbf12b956f76e50347e20d696c6168724b71eee990babd8867`.

The replay used only the standard-library verifier in PR592, with immutable
source pins for PR568, PR569, PR571, PR575 and PR583. PR592's own provenance
and AI disclosure are retained: Claude Opus 5.5 (Anthropic) performed the
submitted construction, while this replay and certificate were prepared with
OpenAI Codex assistance.

This remains conditional on the inherited all-size compiler, common-label /
mutable-source realization, whole-call hosting, precision/tape/exact
recovery, and analytic transfer. It is not an unconditional theorem or full
Lean certification.
