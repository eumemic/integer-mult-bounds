# Independent verification receipt for the R740/rank138 replica32 candidate

κ = 0.001138823042306561 = 1138823042306561/10^18.

This receipt is a fresh verification of PR #443 (`5a514e94f156edcc5fd827b87494d962f79d0f6c`) on top of its frozen candidate package. The local projector and residual-route audit was rerun with Python's standard-library `fractions.Fraction`: every 8x8 frame projector was formed by exact rational Gauss-Jordan inversion, with no floating-point arithmetic and no SymPy dependency. It checked 944 source frames, 3,364 nested forward pairs, the 3,364 reflected pairs, all 16 residual isometries, entrance rank 138, 26,019 exact bank families, the complete profile, and all fourteen mutation controls.

A clean source-bound rerun of `global_kernel.py` reproduced the template and emitted-program digest, all 288 local calls, 213,120 helper assignments, 2,891 banks per stage, 7,620 restored unbanked scalar columns, 123 prefix bits, and deficit 9,984. The unchanged `compose_kernel.py` then passed the two exact rational moment engines, finite invoice, six bootstrap levels, all 47 strict outer inequalities, and rejection of the adjacent 10^-18 grid point plus zero/unit parameter controls. The composed result is bit-bound with the cited PR #433 complex endpoint and has the exact κ above.

This is a finite conditional construction. The PR #433 complex supplier and its analytic/all-size interfaces remain cited dependencies. PR #444's later idle-data hosting extension is deliberately excluded here because its hosted operator and dirty-restoration lemma still require an explicit scalar replay.

Prepared with substantial OpenAI Codex assistance. Earlier source licenses, notices, provenance, and disclosures remain in the unchanged candidate package.
