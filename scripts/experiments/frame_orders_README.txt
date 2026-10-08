Per-group point orders under the PR57 joint frame compiler
=========================================================

Conditional local witness: kappa = 4686464919 / 10^14 > 2^-15,
0.3645% above PR57 (4669442391 / 10^14). Bit saving 4686684559 / 10^14.

Change: PR53's skip-prefix local producer is mapped into each common-point
group through its own pinned point order (certificates/frame-orders-{23,25}.json)
instead of RaD's alternating order; the PR57 compiler then runs unchanged
(frame_orders_compiler.py only swaps the graph). The orders came from simulated
annealing on the role count R = c + q - matched of the uncompiled graph.

Roles: h23 31,416 -> 31,274; h25 41,264 -> 41,107. W 153,481,944 -> 152,877,297.

Verify:   python3 scripts/experiments/verify_frame_orders.py   (make frame-orders-verify)
It replays both serialized words on every input and dirty basis vector in both
orientations, reconstructs every transition, recomputes all fixed-I+J profiles
with CRT checks, and checks the exact recurrence, 47 strict assembly
inequalities, seven margins and eventual cutoffs. Regenerate a word with
python3 scripts/experiments/frame_orders_compiler.py --h 23 --output OUT.json --word WORD.json.gz

Credits: the PR57 joint frame compiler (eumemic with OpenAI Codex assistance),
PR53 skip-prefix producer (Avi Eisenberg / ikeboy with Anthropic Claude
assistance) and every predecessor credited in PR57. Per-group orders by eumemic
with Anthropic Claude assistance.
