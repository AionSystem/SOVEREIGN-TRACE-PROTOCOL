# EPISTEMIC DEBT SCORE — PUBLIC FORMULA

**Document:** EDS-v1.1 (Red-Team Enhanced)
**Governing Standard:** FROZEN-4.0
**Architect:** Sheldon K. Salmon — AI Reliability & ADI Architect
**Effective:** March 2026
**PDE Diagnostic:** v0.5 Deep Profile · 148 findings addressed
**FSVE Integration:** v4.3 Epistemic State Machine
**RMF Cross-Pollination:** v0.6 Structural Patterns
**Convergence Tag:** `M-MODERATE` — requires FCL entries ≥ 5 for `M-STRONG`

---

## TABLE OF CONTENTS

1. [What the EDS Is](#1-what-the-eds-is)
2. [What the EDS Is Not](#2-what-the-eds-is-not)
3. [Definitions](#3-definitions)
4. [The Threshold Rule](#4-the-threshold-rule)
5. [The Formula — Five Components](#5-the-formula--five-components)
6. [Status Labels](#6-status-labels)
7. [Display Format](#7-display-format)
8. [What the Score Does Not Measure](#8-what-the-score-does-not-measure)
9. [Independent Verification](#9-independent-verification)
10. [Scoring Cadence](#10-scoring-cadence)
11. [Nullification Boundary Protocol](#11-nullification-boundary-protocol)
12. [Limitations & Declared Boundaries](#12-limitations--declared-boundaries)
13. [Red Team Resolution Log](#13-red-team-resolution-log)
14. [Appendix A — Ledger JSON Schema](#appendix-a--ledger-json-schema)
15. [Appendix B — Cryptographic Specification](#appendix-b--cryptographic-specification)
16. [Appendix C — Appeal & Dispute Resolution](#appendix-c--appeal--dispute-resolution)

---

## 1. WHAT THE EDS IS

The **Epistemic Debt Score (EDS)** is a 0–100 metric measuring an organization's AI epistemic integrity at a point in time.

It does not measure whether AI systems fail. *They always fail.* Every system, every deployment, every scale.

It measures whether an organization has built the infrastructure and discipline to:

- Document failures honestly before remediation begins
- Resolve them completely and verifiably
- Close critical issues faster than low-priority ones
- Improve over time rather than stagnate
- Report proactively rather than reactively

> **Foundational Principle:** An organization that fails often and resolves honestly scores higher than one that reports nothing. Silence is not a clean record. It is an unscored one.

---

## 2. WHAT THE EDS IS NOT

> **FSVE Law 3 — Scores Are Claims:** The EDS is a claim about organizational epistemic discipline, not a measurement of AI safety, reliability, or performance.

### Hard Boundaries

| The EDS Is NOT | Why This Matters |
|---|---|
| A Safety certification | Safety requires operational evidence, not epistemic audit |
| A Reliability metric | Reliability is system behavior; EDS is organizational behavior |
| A Performance benchmark | Performance is output quality; EDS is documentation quality |
| A Compliance assessment | Compliance is legal; EDS is epistemic |
| A Quality assurance | QA is process verification; EDS is honesty verification |

**FSVE Integration:** The EDS maps to FSVE v4.3's Process Quality Axis. It measures the quality of the measurement process itself. High EDS demonstrates epistemic discipline — it does not guarantee safe AI systems, only honest documentation of their failures.

---

## 3. DEFINITIONS

> **FSVE ODR — Operational Definition Registry**

### Failure

Any deviation from expected AI system behavior that is:

- **(a)** Observable by users or monitoring systems
- **(b)** Documented in the ledger with timestamp and context
- **(c)** Classified by severity: `CRITICAL` / `HIGH` / `MEDIUM` / `LOW`

### Severity Classification

| Level | Definition |
|---|---|
| `CRITICAL` | System crash, data loss, security breach, or harm to users |
| `HIGH` | Major functionality loss, significant performance degradation |
| `MEDIUM` | Minor functionality loss, noticeable performance issues |
| `LOW` | Cosmetic issues, minor inconveniences, edge cases |

### Near-Miss

An event that would have been a failure but was prevented by automated safeguards, human intervention, or favorable external conditions.

**Required documentation:**
- What would have happened
- What prevented it
- When it occurred
- Who or what detected it

### Remediation

A verified fix that:

- **(a)** Addresses the root cause
- **(b)** Is documented with evidence
- **(c)** Is tested to confirm the failure does not recur
- **(d)** Is signed off by the Architect or designated reviewer

### Remediation Status Taxonomy

| Status | Meaning |
|---|---|
| `REMEDIATION FILED` | Fix proposed but not verified |
| `REMEDIATION VERIFIED` | Fix tested and confirmed |
| `REMEDIATION SUPERSEDED` | Fix replaced by better solution |
| `REMEDIATION REVERTED` | Fix caused new issues, rolled back |

### Deployment Scale

The total volume of AI interactions in the assessment period (API calls, user sessions, model inferences, etc.). Must be corroborated by infrastructure logs, billing records, third-party analytics, or Architect audit.

### Domain Risk Classification

| Domain | Risk Level |
|---|---|
| Healthcare / Medical, Defense / Security | `CRITICAL` |
| Financial Services, Critical Infrastructure | `HIGH` |
| Consumer Applications | `MEDIUM` |
| Internal Tools, Research / Experimental | `LOW` |

> **Multi-Domain Organizations** use the highest risk level across all deployments.

### Organization

The legal entity or clearly bounded division being assessed. Must have a defined boundary, governance structure, ledger ownership, and Architect relationship.

### Architect

Sheldon K. Salmon or a designated successor who has:
- Completed the Architect Certification Protocol (ACP)
- Maintained active status
- No conflicts of interest
- Access to all ledger data

**Succession Protocol:** If unavailable for more than 30 days, Deputy Architect assumes role. If no Deputy, AION Council appoints interim.

### Ledger

An append-only, cryptographically sealed record of all failures, near-misses, and remediations in JSON format with:
- Timestamps (UTC)
- SHA-256 hash chain sealing
- Daily backups

### Seal

A SHA-256 hash computed over canonical JSON serialization — UTF-8, LF line endings, alphabetically sorted keys, stripped whitespace.

### Tier

| Tier | Engagement Level |
|---|---|
| Tier 1 | Single point-in-time score |
| Tier 2 | Annual score + recertification |
| Tier 3 | Annual + quarterly trends |
| Tier 4 | Quarterly + monthly monitoring |

---

## 4. THE THRESHOLD RULE

**The EDS does not activate below the minimum ledger threshold.**

> **Minimum threshold:** At least 1 sealed failure with at least 1 remediation attempt on record.
>
> **Below this threshold:** `UNSCORED — insufficient ledger data`

**Why This Rule Exists (FSVE Law 4 — Assumption Load):** A zero-failure ledger in a live AI deployment is not evidence of quality. It is evidence of:

- Poor monitoring
- Under-reporting
- Ledger manipulation
- Insufficient testing
- Organizational silence

**Falsification Condition (NBP-EDS-01):** If an organization with zero documented failures for 24+ months is later found to have had multiple unreported failures, the threshold rule is validated.

### Edge Case: Long-Running Zero-Failure Organizations

If an organization has operated for 5+ years with zero documented failures, an **Architect Audit** is required. Outcomes:

| Finding | Result |
|---|---|
| Genuine Zero Failures | Extremely rare. Architect may grant `EXCEPTIONAL ZERO` status |
| Under-Reporting | Score remains `UNSCORED` until ledger populated |
| Ledger Manipulation | Flagged `EPISTEMIC BAD ACTOR`, barred for 5 years |

---

## 5. THE FORMULA — FIVE COMPONENTS

```
Total EDS = C1 + C2 + C3 + C4 + C5
Maximum:  100 points (20 per component)
```

> **Component Independence Declaration (FSVE Law 3 — CDF):**
> C2 (Remediation Rate) and C4 (Trend Direction) are correlated.
> C1 (Completeness) and C5 (Proactive Reporting) reflect similar organizational culture.

---

### C1 — Completeness `(0–20)`

**Assessment type:** Architect-assessed. Sealed in certification report. Cannot be self-computed.

**Core question:** Does the ledger volume reflect the actual scale of the organization's AI deployment?

**Assessment inputs:** Declared deployment scale · Ledger volume · Domain risk classification · Monitoring coverage · Testing frequency

#### Assessment Protocol

**Step 1:** Compute Expected Failure Rate
```
Expected Failures = Deployment Scale × Industry Base Rate × Risk Multiplier
```

**Step 2:** Compute Completeness Ratio
```
Completeness Ratio = Ledger Volume / Expected Failures
```

**Step 3:** Score by ratio band

| Completeness Ratio | Score |
|---|---|
| 0.80 – 1.20 | 20 — Proportionate |
| 0.60 – 0.79 or 1.21 – 1.50 | 15 – 18 — Slightly thin / thick |
| 0.40 – 0.59 or 1.51 – 2.00 | 10 – 14 — Significantly off |
| < 0.40 or > 2.00 | 0 – 9 — Implausible |

> Architect may adjust ±2 points based on documentation quality and transparency.

---

### C2 — Remediation Rate `(0–20)`

**Assessment type:** Computed directly from ledger JSON. Fully automatable.

```
C2 = (REMEDIATION VERIFIED count / total sealed failures) × 20
     Rounded to nearest integer
```

| Verified Rate | Score |
|---|---|
| 100% | 20 |
| 90 – 99% | 18 |
| 75 – 89% | 15 |
| 50 – 74% | 10 |
| 25 – 49% | 5 |
| Below 25% | 0 – 4 |

**Anti-Gaming:** If more than 50% of filed failures are trivial, the **Trivial Failure Penalty** applies:

```
C2 adjusted = C2 × (1 − Trivial Ratio × 0.5)
```

---

### C3 — Severity Discipline `(0–20)`

**Assessment type:** Computed from ledger JSON with time delta. Fully automatable.

**Method:** Starts at 20. Deductions applied per open high-severity item beyond resolution window.

| Severity | Resolution Window | Penalty Per Overdue Item |
|---|---|---|
| `CRITICAL` | 30 days | −4 |
| `HIGH` | 60 days | −2 |
| `MEDIUM` | 90 days | −1 |

> Floor: 0. Resolution windows based on industry best practices (NBP-EDS-02).

**Severity Classification Audit:** Architect samples 10% quarterly. Misclassification penalty applies.

---

### C4 — Trend Direction `(0–20)`

**Assessment type:** Computed from ledger JSON across two periods.

```
Trend = current period remediation rate − prior period remediation rate
```

| Trend Delta | Score | Status |
|---|---|---|
| > +5% | 20 | Improving |
| −5% to +5% | 10 | Stable |
| < −5% | 0 | Worsening |
| First assessment (provisional) | 10 | — |

**Anti-Gaming:** **Burst Filing Penalty** applies if filings in the last 7 days exceed 30% of total.

---

### C5 — Proactive Reporting `(0–20)`

**Assessment type:** Architect-assessed with ledger input.

#### Automatable Sub-Component: Near-Miss Count

```
Near-miss score = min(near-miss count × 4, 20)
```

| Near-Misses Filed | Score |
|---|---|
| 0 | 0 |
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |
| 5 or more | 20 |

#### Architect-Assessed Adjustment

| Condition | Adjustment |
|---|---|
| Disclosure filed before regulatory deadline | +2 each (cap: +4) |
| Disclosure filed under pressure or post-deadline | +0 |

> **Near-Miss Inflation Penalty** applies if more than 30% of sampled near-misses are invalid.

---

## 6. STATUS LABELS

| Score Range | Status Label | FSVE State |
|---|---|---|
| 90 – 100 | `CERTIFIED CLEAN` | `VALID` |
| 75 – 89 | `EPISTEMIC DEBT MANAGEABLE` | `DEGRADED acceptable` |
| 50 – 74 | `EPISTEMIC DEBT OUTSTANDING` | `DEGRADED concerning` |
| Below 50 | `UNCERTIFIABLE` | `SUSPENDED` |
| Below threshold | `UNSCORED — insufficient ledger data` | `UNCERTIFIED` |

---

## 7. DISPLAY FORMAT

### Public-Facing Badge

```
EDS: 87/100 — EPISTEMIC DEBT MANAGEABLE
Verified by Sheldon K. Salmon · March 2026 · Seal: SHA-256
```

### Dashboard Display (Tier 2+)

```
EPISTEMIC DEBT SCORE — Organization Name
Assessment date: March 7, 2026
Period: January 1 – March 7, 2026

C1  Completeness            18 / 20
C2  Remediation Rate        16 / 20   (12 of 15 failures remediated)
C3  Severity Discipline     20 / 20   (0 overdue critical/high items)
C4  Trend Direction         20 / 20   (+12% improvement from Q4 2025)
C5  Proactive Reporting      8 / 20   (2 near-misses filed)
    ─────────────────────────────────
    TOTAL                   82 / 100

Status: EPISTEMIC DEBT MANAGEABLE
Seal:   SHA-256 of this report
```

### ScoreTensor Integration (FSVE v4.3)

```json
{
  "id": "UUID v4",
  "timestamp": "ISO 8601",
  "fsve_version": "4.3",
  "score_type": "VALIDITY",
  "measurement_class": "EVALUATIVE",
  "value": 0.82,
  "validity_status": "DEGRADED",
  "uncertainty_mass": 0.15,
  "Uq": 0.75,
  "Cq": 0.40,
  "rqs_score": 0.88,
  "rqs_label": "HIGH",
  "scc_status": "SCORED"
}
```

---

## 8. WHAT THE SCORE DOES NOT MEASURE

The EDS measures **epistemic integrity** — not AI safety, quality, or legal standing.

| Out of Scope | Reason |
|---|---|
| Whether AI systems are safe or reliable | Requires operational evidence, not documentation audit |
| Whether failures caused harm | Harm assessment is a separate process |
| Whether the organization is legally compliant | Legal compliance is not epistemic integrity |
| Whether remediation strategies were effective | Effectiveness is a performance question |
| Content accuracy of any sealed record | The EDS verifies documentation discipline, not content truth |

> **The EDS is a grade on the organization's relationship with truth about that system — not a grade on the system itself.**
> See `NON-RECOURSE-STATEMENT.md` for the full scope boundary.

**FSVE Law 6 — Explainability Requirement:** The EDS provides full decomposition. Each component scored independently, all penalties documented, residual uncertainty mass declared, audit trace ID enables replication.

---

## 9. INDEPENDENT VERIFICATION

Three of the five components — **C2, C3, and C5 base** — are computed directly from public ledger JSON and are independently verifiable.

```bash
python3 score.py --ledger ./ledger/ --org "Organization Name"
```

> `score.py` is a commercial deliverable (Tier 2+). The formula is public. The tool is proprietary.

**Components C1 and C5 (architect-adjusted)** are sealed in the Certification Report. The seal is the verification. The report cannot be altered after sealing.

### Verification Protocol (FSVE Gate Integration)

1. Compute C2, C3, C5 base from ledger JSON
2. Compare to Certification Report values
3. If match within ±1 point → **Verification successful**
4. If mismatch > 1 point → Flag `SEAL CHAIN DISCREPANCY` → Escalate to Architect

---

## 10. SCORING CADENCE

| Tier | Cadence | Context Half-Life |
|---|---|---|
| Tier 1 | Single point-in-time at engagement | 90 days |
| Tier 2 | Annual, updated at recertification | 180 days |
| Tier 3 | Annual + quarterly trend updates | 90 days |
| Tier 4 | Quarterly + monthly trend monitoring | 30 days |

**FSVE Law 5 — Context Drift:** EDS scores decay over time.

```
EDS_valid(t) = EDS_initial × exp(−Decay Rate × Δt)
```

| Freshness Value | Status |
|---|---|
| ≥ 0.80 | `FRESH` |
| 0.60 – 0.79 | `AGING` |
| 0.25 – 0.59 | `STALE` |
| < 0.25 | `EXPIRED` |

---

## 11. NULLIFICATION BOUNDARY PROTOCOL

| NBP ID | Rule | Strategic CF | Falsification Condition |
|---|---|---|---|
| NBP-EDS-01 | Zero-failure threshold rule | 50 | If zero-failure orgs consistently demonstrate high integrity when failures are discovered, rule requires revision |
| NBP-EDS-02 | Resolution windows (30 / 60 / 90 days) | 45 | If shorter windows (15 / 30 / 60) yield significantly better outcomes, windows require revision |
| NBP-EDS-03 | Industry base rates for C1 | 40 | If actual failure rates diverge from base rates by > 50% across 10+ orgs, recalibrate |
| NBP-EDS-04 | Component weights (20 points each) | 40 | If alternative weightings correlate more strongly with outcomes, revise |
| NBP-EDS-05 | Trend delta threshold (5%) | 35 | If a different threshold better predicts improvement, revise |

---

## 12. LIMITATIONS & DECLARED BOUNDARIES

### Formal Scope (PDE Section 14)

**Within Scope:**
- Organizations with AI deployments
- Ledger-based failure tracking
- Architect-assessed epistemic integrity

**Outside Scope (Declared):**
- AI system safety / reliability
- Legal compliance
- Technical quality of remediations
- Cross-organizational comparison (no normalization)
- Real-time monitoring
- Small organizations (< 10 employees)
- Non-English speaking organizations
- Organizations in authoritarian regimes

### Declared Uncertainty

> **FSVE Meta-Law 1 — No Recursive Certainty:** The EDS cannot claim certainty about its own certainty. All EDS scores carry `measurement_class = EVALUATIVE` with `uncertainty_mass ≥ 0.15` until FCL entries demonstrate empirical calibration.

### Goodhart's Law Acknowledgment

*"When a measure becomes a target, it ceases to be a good measure."*

**Mitigations:**
- Architect assessment detects gaming
- Anti-gaming penalties for trivial failures and burst filings
- Near-miss verification
- Severity audits
- Continuous metric improvement

---

## 13. RED TEAM RESOLUTION LOG

**PDE v0.5 Deep Profile Scan — 148 Total Findings**

| Category | Count |
|---|---|
| Resolved / Fixed | 132 |
| Accepted Risk | 12 |
| Architect Directed | 4 |
| **Unresolved** | **0** |

**Resolved Fixed (132):** ODR definitions, NBP, FSVE integration, edge cases, processes, theoretical foundation, schema, cryptographic specification, temporal details, scope, anti-gaming, uncertainty, sensitivity analysis, validation.

**Accepted Risk (12):** Architect bias, cost barrier, language barrier, Goodhart's Law, cross-org comparison.

**Architect Directed (4):** Proprietary tool, cost structure, cryptographic library, Deputy Architect succession.

---

## APPENDIX A — LEDGER JSON SCHEMA

### Required Fields

| Field | Type | Constraint |
|---|---|---|
| `entry_id` | UUID | Version 4 |
| `timestamp` | String | ISO 8601 |
| `entry_type` | Enum | `FAILURE` / `NEAR_MISS` / `REMEDIATION_FILED` / `REMEDIATION_VERIFIED` |
| `severity` | Enum | `CRITICAL` / `HIGH` / `MEDIUM` / `LOW` |
| `description` | String | Minimum 50 characters |
| `seal` | String | SHA-256 |

### Optional Fields

| Field | Description |
|---|---|
| `context.system` | System identifier |
| `context.environment` | Deployment environment |
| `context.user_impact` | Description of user impact |
| `context.detected_by` | Detection method or actor |
| `remediation.root_cause` | Root cause analysis |
| `remediation.fix_description` | Description of fix applied |
| `remediation.evidence` | Array of evidence artifacts |
| `remediation.test_results` | Verification test output |
| `remediation.verified_by` | Reviewer name or ID |
| `remediation.verified_at` | ISO 8601 timestamp |
| `previous_entry_hash` | SHA-256 of prior entry seal |

---

## APPENDIX B — CRYPTOGRAPHIC SPECIFICATION

### Seal Computation

```python
import hashlib
import json

def compute_seal(entry: dict) -> str:
    # Step 1: Canonicalize — sort keys, strip whitespace, UTF-8, LF line endings
    canonical = json.dumps(entry, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    canonical = canonical.replace('\r\n', '\n').replace('\r', '\n')
    # Step 2: Compute SHA-256
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()
```

### Hash Chain

Each entry includes `previous_entry_hash` pointing to the prior entry's seal. This creates an immutable, tamper-evident chain.

### Chain Verification

```python
def verify_chain(ledger: list) -> bool:
    for i, entry in enumerate(ledger):
        if i > 0:
            if entry.get('previous_entry_hash') != ledger[i-1]['seal']:
                return False
        if entry['seal'] != compute_seal(entry):
            return False
    return True
```

---

## APPENDIX C — APPEAL & DISPUTE RESOLUTION

### Appeal Process

1. Organization submits written appeal within **30 days** specifying: disputed components, evidence, and proposed resolution
2. Architect reviews within **14 days** and issues written decision
3. If denied, organization may escalate to AION Council

### Dispute Resolution

If Architect and organization cannot agree, AION Council appoints an independent reviewer. The reviewer conducts a fresh assessment. Decision is binding. Costs borne by losing party.

### Revocation Process

Certification may be revoked for:
- Ledger manipulation
- Material misrepresentation
- Failure to maintain ledger
- Compromised epistemic integrity

**Process:**
1. Architect issues `REVOCATION NOTICE` with rationale
2. Organization has 30 days to respond
3. If inadequate: certification revoked, organization barred for 12 months, public notice issued (Tier 2+)

---

## DOCUMENT INTEGRITY

```
Architect:         Sheldon K. Salmon — AI Reliability & ADI Architect
Contact:           aionsystem2026@gmail.com
Repository:        github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL
Governing Standard: FROZEN-4.0
PDE Diagnostic:    v0.5 Deep Profile · 148 findings · 0 unresolved
FSVE Integration:  v4.3 Epistemic State Machine
RMF Pollination:   v0.6 Structural Patterns
Canonical Form:    JSON-sorted · UTF-8 · LF-normalized
SHA-256 Seal:      To be computed after final red-team review
```

---

*Epistemic debt is not failure. It is the gap between what happened and what was documented. The EDS closes that gap.*
