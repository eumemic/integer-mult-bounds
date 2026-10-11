# Provenance and assistance

All source material is Apache-2.0; original headers and notices remain intact.

* PR443, chafreaky / Chafik Boukhalfa, with OpenAI Codex assistance, head
  `5a514e94f156edcc5fd827b87494d962f79d0f6c`: the complete rank138, 32-replica
  non-hosting package is vendored unchanged in `e8-r740-replica32/`. Its 118
  file blobs are pinned individually in `SOURCES.json`; its own manifest,
  predecessor source pins, notices and license are retained.
* PR450, DreamingOfClouds, with Claude Opus 5.5 (Anthropic) via Claude Code,
  head `6faca41020a620689de013cdab9f61a22deca314`: `mix_target.py`,
  `mix_check.py` and the original `BIT-LABEL-LEMMA.md` are vendored unchanged
  in `vendor450/`. They are credited for discovery and implementation of
  the target-prefix mixer, including its scalar checks.
* Retained contributions include eumemic PR436/440/441, chafreaky's response
  kernel lineage, icekylinx PR433, Zhihao Chen / jacklightChen PR386/425,
  Dylan Crow's PR370 producer, ai-nanachi's retiming and reset work,
  Jacob Sussman's E8 unit, and all authors named in the parent notices.

The present non-hosting composition, finite bit-address-label proof,
standard-library independent operator audit, portable verification wrapper,
new exact invoice/assembly and integration were prepared for eumemic with
substantial OpenAI Codex assistance. The unchanged PR450 note records the
original unresolved review question; `PROOF.md` supplies the new finite
local argument. The package does not import PR450's hosting construction.

PR443, PR450 and all earlier published heads and claims remain frozen.
