# Bit target mixing without idle hosting

This note closes the finite local label question for the target-prefix mixer from
DreamingOfClouds's PR450 on the banked PR443 word. It does not admit the cross-copy
hosting in PR448/450/453. Original PR443 and PR450 provenance and disclosures must
be retained. This independent argument and checker were prepared with OpenAI Codex
assistance; Apache-2.0.

The actual inherited bit address operator, from PR386's geometry interface, is

`D_P = [[I-P,P],[P,I-P]]`.

Here P is the rational orthogonal projector of the current frame, defined over
each admitted odd address field. D_P is an involution. In the sum/difference
coordinates `(x+y,x-y)`, its two blocks are I and `R_P = I-2P`. Therefore checking
the R blocks is an exact check of the full doubled address matrix, not an analogy
with a scalar register circuit. For nested P <= Q,

`D_(Q-P) D_P = D_Q`,

and on the reflected path the same child satisfies

`D_(Q-P) D_(I-Q) = D_(I-P)`.

For a bit array f on the doubled address set, define its address pullback by
`(Lambda_P f)(z) = f(D_P z)`. This is a linear operator over F2. Its definition
depends only on P and the actual address chart; it does not depend on whether f
is designated a source, a target, or a helper. In a local invocation, the inherited
data/port routes bring the ADD operands to the common local chart. The mixer
does not change those routes or the bank ownership.

Every target begins at frame 0, so its literal sequence of MOVE address factors
telescopes to D_P when its current frame is P. Thus the two target operands at a
mix gate in G carry the same actual pullback Lambda_G. For arbitrary bit arrays
a and b, including correlated dirty contents,

`Lambda_G(a xor b) = Lambda_G(a) xor Lambda_G(b)`.

This establishes the new target-to-target ADD with no assumption that an original
helper and a target have the same initial label. More generally the standard
label invariant is `physical_r = Lambda_current_r(formal_r)`, with initial formal
arrays `Lambda_start_r^-1(physical_input_r)`. A MOVE preserves it by the exact
projector identity above, an ADD preserves it by common-pullback linearity, and
the inherited COPY/scatter/ERASE schedule preserves it by its charged transport
between source and scatter labels. Consequently a scalar word M lifts to the
array operator `diag(Lambda_final) M diag(Lambda_start)^-1`. Since the mixed word
has the same scalar M and identical start/final frames as PR443, it has exactly
the same full local array operator on all inputs. The separate all-column scalar
check includes arbitrary source, target, and dirty-helper inputs.

The checker verifies equality of the original and mixed word's entire frame
list, root-line list, starts, finals, retained totals, and A/C phases. No new
rational frame or address denominator is introduced; the inherited original
frame prime admission applies. The matrices are compared over Q and so the
identities descend to every address field admitted by those original witnesses.

The reflected program has complemented labels, reversed MOVE factors, inverse
ADD coefficients, and the inherited fresh-COPY convention. Both operands of each
new reflected ADD have the same label I-G; the second projector identity proves
the required actual path. F2 inverse ADD is again XOR. This closes the same local
operator identity in both orientations.

The independent standard-library checker `code/operator_audit.py` reconstructs
actual participant MOVE chronology directly from the mixed word, forms exact
rational projectors, verifies every used nested and reflected factor identity,
and verifies the labels at all 92 new target ADDs (46 frame-0 preconditioners and
46 B-phase mixes). Its Boolean orbit check exhausts all inputs on both possible
orbit types of an address involution (fixed points and two-cycles), proving the
pullback identity for arbitrary arrays without a randomness assumption. Controls
reject a mismatched operand label and an omitted nonzero child. It is an operator
admission check. It also independently replays all 980 scalar columns for both
the original and mixed words, in forward and inverse order, closing copied work
and restoring all 740 arbitrary dirty-helper columns. Paid profiles, complete
global bank ownership, finite invoices, both rational moments, and final exact
assembly remain separate and must be checked before publication.

The standalone command is:

`python operator_audit.py --word MIXED_WORD --parent ORIGINAL_WORD --out REPORT`

Both words may be plain JSON or gzip-compressed JSON; no third-party dependency
is used. The checker generates no hosted owner and assumes no cross-family
residual splitting.

Scope remains the inherited finite conditional compiler framework. No all-size
compiler theorem or unconditional multiplication theorem is asserted here.
