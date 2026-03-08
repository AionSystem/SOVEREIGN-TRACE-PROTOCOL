# EPISTEMIC DEBT SCORE
## Sovereign Trace Protocol — AI Epistemic Integrity Metric

```
╔══════════════════════════════════════════════════════════════════╗
║   ⬡  SOVEREIGN TRACE PROTOCOL  ⬡                                ║
║   Epistemic Debt Score · Public Formula · FROZEN-2.0            ║
║   Architect: Sheldon K. Salmon · AI Reliability & AGI Architect ║
╚══════════════════════════════════════════════════════════════════╝
```

**Document Version:** EDS-v1.0
**Governing Standard:** FROZEN-2.0
**Effective:** March 2026

---

## WHAT THE EPISTEMIC DEBT SCORE IS

The Epistemic Debt Score (EDS) is a 0–100 metric measuring an
organization's AI epistemic integrity at a point in time.

It does not measure whether AI systems fail.
They always fail. Every system, every deployment, every scale.

It measures whether an organization has built the infrastructure
and discipline to:
- Document failures honestly before remediation begins
- Resolve them completely and verifiably
- Close critical issues faster than low-priority ones
- Improve over time rather than stagnate
- Report proactively rather than reactively

An organization that fails often and resolves honestly
scores higher than one that reports nothing.
Silence is not a clean record. It is an unscored one.

---

## THE THRESHOLD RULE

**The EDS does not activate below the minimum ledger threshold.**

Minimum threshold: at least 1 sealed failure with at least
1 remediation attempt on record.

Below this threshold: `UNSCORED — insufficient ledger data`

This rule exists to prevent the most dangerous outcome:
an organization with zero documented failures claiming
a perfect score. A zero-failure ledger in a live AI
deployment is not evidence of quality. It is evidence
of nothing.

---

## THE FORMULA — FIVE COMPONENTS, 20 POINTS EACH

**Total EDS = C1 + C2 + C3 + C4 + C5**
**Maximum: 100**

---

### C1 — Completeness (0–20)
**Architect-assessed. Sealed in certification report.**

Does the ledger volume reflect the actual scale of the
organization's AI deployment?

An organization running 10,000 AI interactions per day
with 2 sealed failures over 12 months has a completeness
problem — not a quality problem.

Assessment inputs required:
- Declared deployment scale (interactions per period)
- Ledger volume (sealed entries per period)
- Domain risk classification (healthcare/defense/consumer/other)

This component cannot be self-computed. It requires the
Architect's assessment of proportionality. It is the
component that cannot be gamed by filing more issues.
Filing accurately earns C1. Filing minimally loses it.

| Assessment | Score |
|-----------|-------|
| Ledger volume proportionate to deployment scale and domain risk | 20 |
| Ledger volume plausible but thin relative to deployment scale | 10–15 |
| Ledger volume implausibly low for declared deployment scale | 0–9 |

---

### C2 — Remediation Rate (0–20)
**Computed directly from ledger JSON. Fully automatable.**

What fraction of sealed failures have verified remediations?

```
C2 = (REMEDIATION_VERIFIED count / total sealed failures) × 20
```

Rounded to nearest integer.

| Remediation Rate | Score |
|-----------------|-------|
| 100% | 20 |
| 90–99% | 18 |
| 75–89% | 15 |
| 50–74% | 10 |
| 25–49% | 5 |
| Below 25% | 0–4 |

`REMEDIATION_VERIFIED` requires Architect sign-off on the
remediation record. `REMEDIATION_FILED` (pending) counts as
0 for C2 until verified. Self-certification does not exist.

---

### C3 — Severity Discipline (0–20)
**Computed from ledger JSON with time delta. Fully automatable.**

Are critical and high severity failures being closed faster
than low-priority ones?

Starts at 20. Deductions applied per open high-severity item
beyond the resolution window.

| Condition | Deduction |
|-----------|-----------|
| CRITICAL severity unresolved > 30 days | −4 per item |
| HIGH severity unresolved > 60 days | −2 per item |
| MEDIUM severity unresolved > 90 days | −1 per item |

Floor: 0. Cannot go negative.

This component rewards triage discipline — prioritizing
the failures that matter most. An organization can have
many open LOW items and still score well on C3.
One unresolved CRITICAL for 90 days destroys C3.

---

### C4 — Trend Direction (0–20)
**Computed from ledger JSON across two periods. Automatable after first renewal.**

Is the organization's epistemic integrity improving, stable,
or worsening relative to the prior assessment period?

Requires at least two assessment periods to compute.
First-time certifications receive a provisional 10 pending
the second period.

```
Trend = current_period_remediation_rate - prior_period_remediation_rate
```

| Trend | Score |
|-------|-------|
| Improving (delta > +5%) | 20 |
| Stable (delta −5% to +5%) | 10 |
| Worsening (delta < −5%) | 0 |
| First assessment (provisional) | 10 |

Trend is the only component that rewards sustained commitment
over time. An organization can game a single assessment by
filing a burst of remediations before scoring. They cannot
game two consecutive periods of trend data.

---

### C5 — Proactive Reporting (0–20)
**Architect-assessed with ledger input. Partially automatable.**

Does the organization report before they are required to?
Near-misses, pre-pressure disclosures, and voluntary filings
before regulatory deadlines are the strongest epistemic
integrity signal in the entire score.

Automatable sub-component: near-miss count from ledger
```
Near-miss score = min(near_miss_count × 4, 20)
```

Architect-assessed adjustment:
- Disclosures filed before regulatory deadline: +2 each (cap +4)
- Disclosures filed under pressure or post-deadline: 0

| Near-Miss Count | Base Score |
|----------------|------------|
| 0 | 0 |
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |
| 5+ | 20 |

An organization that files near-misses is an organization
that has built an honest internal reporting culture.
That signal is worth more than a clean failure log.

---

## STATUS LABELS

| EDS Range | Status |
|-----------|--------|
| 90–100 | ✅ CERTIFIED CLEAN |
| 75–89 | 🟡 EPISTEMIC DEBT MANAGEABLE |
| 50–74 | 🟠 EPISTEMIC DEBT OUTSTANDING |
| Below 50 | 🔴 UNCERTIFIABLE |
| Below threshold | ⬜ UNSCORED — insufficient ledger data |

---

## DISPLAY FORMAT

Public-facing badge display:

```
⬡ EDS: 87/100 · EPISTEMIC DEBT MANAGEABLE
Verified by Sheldon K. Salmon · March 2026 · Seal: [SHA-256]
```

Dashboard display (Tier 2+):

```
EPISTEMIC DEBT SCORE — [Organization Name]
Assessment date: March 7, 2026
Period: January 1 – March 7, 2026

C1  Completeness          18 / 20
C2  Remediation Rate      16 / 20    (12 of 15 failures remediated)
C3  Severity Discipline   20 / 20    (0 overdue critical/high items)
C4  Trend Direction       20 / 20    (+12% improvement from Q4 2025)
C5  Proactive Reporting    8 / 20    (2 near-misses filed)
─────────────────────────────────────
    TOTAL                 82 / 100

Status: 🟡 EPISTEMIC DEBT MANAGEABLE
Seal: [SHA-256 of this report]
```

---

## WHAT THE SCORE DOES NOT MEASURE

- Whether AI systems are safe or reliable
- Whether failures caused harm
- Whether the organization is legally compliant
- Whether remediation strategies were effective
- Content accuracy of any sealed record

The EDS measures epistemic integrity — the discipline of
honest, timely, structured self-documentation.

It is not a grade on the AI system.
It is a grade on the organization's relationship with truth
about that system.

See `NON-RECOURSE-STATEMENT.md` for the full scope boundary.

---

## INDEPENDENT VERIFICATION

Three of the five components (C2, C3, C5 base) are computed
directly from public ledger JSON. Any party with Python 3.11+
and access to the ledger directory can independently verify
these components using `score.py`.

Components C1 and C5 (architect-adjusted) are sealed in the
Certification Report delivered at each tier. The seal is the
verification. The report cannot be altered after sealing.

```bash
# Partial self-verification (C2, C3, C5 base only)
python3 score.py --ledger ./ledger/ --org "Organization Name"
```

`score.py` is a commercial deliverable — available as part of
Tier 2 and above certification engagements. It is not
open-sourced. The formula is public. The tool is proprietary.

---

## SCORING CADENCE

| Tier | EDS Cadence |
|------|-------------|
| Tier 1 | Single point-in-time score at engagement |
| Tier 2 | Annual score, updated at recertification |
| Tier 3 | Annual score + quarterly trend updates |
| Tier 4 | Quarterly score + monthly trend monitoring |

---

*Sheldon K. Salmon · AI Reliability & AGI Architect · March 2026*
*Sovereign Trace Protocol · FROZEN-2.0*
*aionsystem2026@gmail.com*
*github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL*
