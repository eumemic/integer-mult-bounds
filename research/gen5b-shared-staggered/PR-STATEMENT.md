κ = 7.51186773660960e-4

# Shared kernels and staggered target prefixes on weighted gen5b

The conditional finite bound is **κ ≈ 7.51186773660960 × 10⁻⁴**. The exact rational
is `4694917335381/6250000000000000`. This package composes the weighted matching
word with 1,804 kernel entries and 228 target-prefix dependencies, followed by
87 second-descent retimings, 440 early helper restorations and eight terminal
sinks. Every scalar word and complete finite invoice must pass `verify.py`.

The target change preserves all 220 existing rank-21 squares and adds eight
earlier pairs. Seven replace 18+2 paid paths with rank 20; one replaces 17+1 with
rank 18. An early pair can overlap a later square because their dependent targets
are distinct. Setup runs in reverse close order and restoration in close order;
an encoded target must restore before it can serve another dependent. The exact
prefix relations are recomputed from the actual input word. Relative to the
220-square stage, the paid histogram delta is
`{1:-1, 2:-7, 17:-1, 18:-6, 20:+7}`: eight fewer local paid children, unchanged
rank mass and eight additional scalar ADDs. See
[STAGGERED-TARGET-PROOF.md](STAGGERED-TARGET-PROOF.md).

The kernel composition retains all 1,734 entries from the pinned PR300 word and
adds all 70 PR302 shared-donor witnesses after exact logical-role rebinding.
The native transform rechecks literal target responses, original scalar cut
contents, first-frame containment, chronological noninterference and monotone
donor chains. All 87 selected second-descent scalar occurrences are resolved
uniquely by operands, coefficient, category and original rational frame basis.
Restoration and sink selections are freshly screened on the resulting word.

## Verification

```sh
python -m pip install -r research/gen5b-shared-staggered/requirements.txt
python -B research/gen5b-shared-staggered/verify.py \
  --output /tmp/gen5b-shared-staggered-verification
python -B research/gen5b-shared-staggered/gen5bit/producer/regenerate.py \
  --work /tmp/gen5b-shared-staggered-regeneration
```

Use Python 3.11+ and SymPy 1.14.0, with a new output directory outside the
package. Verification is network-free and rejects pin-recording mode. It
recomputes virtual/source decoding, actual scalar words in both directions,
all dirty restoration, both reflected ledgers, native global lowering, exact
projectors and determinant guards, all literal bank assignments, the complete
paid profile and finite invoice, two rational moment engines, all 47 strict
outer inequalities and adjacent-grid rejection. The complete input manifest
must remain unchanged throughout. `verification.json` is the admission result.

The virtual weighted-matching word is unchanged from the pinned PR275 input;
its decompressed SHA256 is
`9144bc371104df43abf65f8fcff7a0f195301118ccb4c37b02799799d9f2eec1`.

## Provenance and scope

[SOURCE.json](SOURCE.json) pins the inputs; [NOTICE.md](NOTICE.md) describes new
and inherited contributions and preserves AI disclosures. Original notices,
proofs, source pins and licenses remain packaged. Prepared with substantial
OpenAI Codex assistance. The inherited all-size interfaces remain assumptions;
this is a conditional finite construction.
