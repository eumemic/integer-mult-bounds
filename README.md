This builds on #5 at commit d3d370c34937503bd3fa63c83d505a05e8e50893 and improves the conditional exponent saving from

$$
\kappa=\frac{1479}{10^{12}}
$$

to

$$
\boxed{\kappa=\frac{15253}{10^{13}}=1.5253\times10^{-9}},
\qquad
T(n)=O!\left(n(\log n)^{1-\kappa}\right).
$$

The improvement in exponent saving is 3.13049%. The construction retains #5’s fast Gaussian resampling, compressed complex network, and conditional proof dependencies. It remains below the next dyadic threshold, $2^{-29}$.

Construction

Fix the ground-point pairs ${0,1},{2,3},\ldots,{48,49}$. For each common point $i$, run the existing local paired circuit on the ordered list consisting of:

1. All points outside ${i,i\mathbin{\mathrm{xor}}1}$, in increasing order.
2. The partner $i\mathbin{\mathrm{xor}}1$ as the final singleton.

This aligns the first-level pair partitions across common-point groups and exposes additional identical supports for sharing.

Quantity	#5	This PR
Local additions	9,813	9,813
Global additions	450,394	435,450
Partial outputs	58,800	58,800
Auxiliary roles per invocation	509,194	494,250
Total bit-network roles $W$	406,321,422,080,000	394,839,648,000,000
Rank deficit $D$	1,767,136,000,000	1,767,136,000,000

Proof outline

Relabeling preserves each local pair-exclusion identity. Every merged node still has a common point, so its rational indicator span remains nondegenerate under the retained form $I-J/9$. Forward support inclusions and reversed orthogonal-complement inclusions therefore retain the frame-transfer hypotheses.

The existing reversible schedule restores arbitrary scratch, and the central gates, stage joins, and data endpoints remain unchanged. Consequently,

$$
s=Wm-D,\qquad m=125000,\qquad
\eta=\frac{D}{Wm}=\frac{23}{642375000}.
$$

An exact rational logarithm enclosure proves

$$
\log125000<\frac{1173607}{100000},
\qquad
\eta>
\frac{30508}{10^{13}}\frac{1173607}{100000}.
$$

Thus the bit network supports $\tau=1-30508/10^{13}$.

Retaining $\sigma=1-14/10^9$, choose

$$
\epsilon=\frac{49999}{100000},\quad
c=\frac{99999}{100000},\quad
\beta=\frac{19}{25},\quad
\zeta=\frac1{10000},\quad
\delta=\frac1{10^6},
$$

$$
C_1=\frac{19601}{10000},\quad
\lambda=1-\frac{305075}{10^{14}},\quad
\lambda’=1-\frac{30507}{10^{13}}.
$$

All recurrence, guard, reservation, and assembly inequalities hold strictly. The seven assembly margins satisfy

$$
\min_i g_i=\frac{1525319493}{10^{18}},
\qquad
\min_i g_i-\kappa=\frac{19493}{10^{18}}>0.
$$

The proof also establishes that this witness exceeds the old bit graph’s assembly ceiling, so the improvement requires the changed graph rather than parameter tuning alone.

Artifacts

* Proof note
* Exact certificate
* Construction and reproduction details
* Independent patch against the pinned upstream manuscript

Verification

python3 scripts/aligned_pair_network.py
make verify
make aligned-note

The completed verification run passed 187 tests, all manuscript patch-application checks, and regeneration of the earlier certificates and patches without changes. The combined manuscript compiled without unresolved references or citations.

The new tests include independent small-case support expansions, every dirty-input basis vector in both invocation directions, shared three-stage scratch restoration, and negative parameter cases.

Prepared with assistance from OpenAI Codex. This is an incremental conditional proof with reproducible finite checks, not independent mathematical review or formal verification of the underlying multiplication theorem. The percentage compares asymptotic exponent savings, not practical runtime.
