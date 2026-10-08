# Annealed point orders for RaD's producers

$$T(n)=O(n(\log n)^{1-\kappa}),\qquad \kappa=\frac{4151607798}{10^{14}}=4.151607798\times10^{-5}>2^{-15}.$$

**0.5373% above PR #50** (`4129418696/10^14`) and 1.1328% above PR #47, on which it builds. Bit saving `4151780164/10^14`.

## Change

PR #47 maps RaD's local producer into every common-point group through one fixed
alternating point order. Here each group gets its own pinned order
(`orders-{h}.json`, which also carries PR #47's summand-swap bits). The orders
were found by simulated annealing on the role count `R = c + q − matched`.
Everything else is PR #47 / #46. The change is independent of the reordered
exclusion sums in PR #48–#50, so the two should stack.

| | PR #47 | This |
|---|---:|---:|
| h=23: R (additions c, matched) | 36,656 (37,098, 5,778) | **36,164** (37,377, 6,549) |
| h=25: R (additions c, matched) | 48,398 (49,169, 7,696) | **47,722** (49,516, 8,719) |
| Width W | 178,168,258 | **175,839,462** |

## Verify

```sh
make annealed-orders-verify
```

`producer.py` replays both producers with PR #43's unchanged checkers: scalar
identity, dense audit, pinned-link profile, independent recount, and the full
timeline with the dirty basis in both orientations. `witness.py` checks the
exact moment, all 47 assembly constraints and 7 margins, rejects the next grid
points, and excludes PR #47's child list. `anneal.py` and
`optimize_matching.py` regenerate the pinned inputs; they are not part of
verification. Full `make verify`: @FULL@.

Credits: Rohan Arun (PR #47), Chafik Boukhalfa (PR #43/#46), RaD / hipotures
(PR #41) and every predecessor credited there. Annealed orders by eumemic with
Anthropic Claude assistance.
