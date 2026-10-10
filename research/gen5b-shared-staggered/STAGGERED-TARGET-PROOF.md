# Staggered target-prefix compression on the gen5b word

This extends eumemic's target-prefix transform retained by PR268 and its
subsequent gen5 adaptations. Prepared with OpenAI Codex assistance. The inherited
Apache-2.0 notices and mathematical assumptions remain in force.

The scalar program uses independent target contents. For an original target t,
write its value after the common cut as y_t + R_t(i), where R_t(i) is the literal
F2 response accumulated strictly after the cut through record i. No selected
original target is a scalar or COPY control before its last selected close.

A dependency t <- S closing at c is admitted only when
R_t(c) = XOR_{p in S} R_p(c), recomputed from the original word, and all operands
fit its nondegenerate close frame. The target t occurs as a dependent only once.
If a donor p is another dependent, p must close strictly before t. Therefore the
dependency graph is acyclic, ordered by close time.

At the common zero-frame cut, emit t -= p for each dependency edge in descending
close order. At this point every donor still carries its original cut value:
any encoded donor closes earlier, so its own setup comes later. Suppress the
original writes to t between the cut and its close. At c, emit t += p in the
common close frame. Every donor that was encoded has now been restored. The
result is y_t - sum(y_p) + sum(y_p + R_p(c)) = y_t + R_t(c) in F2. All later
original writes to t are preserved. Restoration in increasing close order proves
this identity inductively for every dependent. The actual emitted odd-coefficient
word is also replayed forward and backward on every source, target and dirty
formal column; the signed prefix norm is recomputed for finite charging.

All MOVE records are regenerated from surviving and inserted scalar/COPY uses.
A separate frame-path census ignores emitted MOVEs, checks primal nesting and
the reflected annihilator chain, checks each endpoint basis, and recounts paid
rank histograms. Original external input/output frames, helper entrances, dirty
endpoints and copied-center lifetimes are unchanged by this target stage.

## Concrete selection

All 220 existing rank-21 target squares are retained. Eight earlier target pairs
are added; their dependent is distinct from the enclosing square's dependent.
Seven close at rank 20, compressing an 18+2 path to 20. One closes at rank 18,
compressing a 17+1 path to 18. The source and dirty words are unchanged.

Relative to the existing 220-square target stage the paid histogram delta is
{1: -1, 2: -7, 17: -1, 18: -6, 20: +7}. Its rank mass is zero and its number of
paid children is -8 per local invocation. The literal target transform adds eight
weighted scalar instructions net, which the signed replay and finite invoice
must charge.

The dedicated control replay individually omits every one of the 16 new setup
or restoration additions and requires an incorrect endpoint. These supplement
the full transform's forward/inverse all-column replay and its inherited omitted
setup control.

## Search boundary

The information-set screen permits any number of dependent targets with a
minimum-weight retained basis at every scalar-event closure sharing the same
next frame. Actual frame cohorts have at most four targets (rank 21 or below),
two targets at rank 22, and one at rank 23; no cohort crosses cube boundaries.
The rank-22 pair responses have full rank for all sampled prefix closures.
An additional screen over nonzero cuts found positive paid-profile candidates
only within the same eight special cubes. This is a bound on this search class,
not a global optimality statement.
