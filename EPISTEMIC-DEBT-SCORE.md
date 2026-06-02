Epistemic Debt Score - Public Formula - FROZEN-2.0
Architect: Sheldon K. Salmon - AI Reliability & AGI Architect
Document Version: EDS-v1.1 (Red-Team Enhanced)
Governing Standard: FROZEN-2.0
Effective: March 2026
PDE Diagnostic: v0.5 Deep Profile (148 findings addressed)
FSVE Integration: v4.3 Epistemic State Machine
RMF Cross-Pollination: v0.6 Structural Patterns
Convergence Tag: M-MODERATE (requires FCL entries >= 5 for M-STRONG)
WHAT THE EPISTEMIC DEBT SCORE IS
The Epistemic Debt Score (EDS) is a 0 to 100 metric measuring an organization's AI epistemic integrity at a point in time.
It does not measure whether AI systems fail. They always fail. Every system, every deployment, every scale.
It measures whether an organization has built the infrastructure and discipline to:
Document failures honestly before remediation begins
Resolve them completely and verifiably
Close critical issues faster than low-priority ones
Improve over time rather than stagnate
Report proactively rather than reactively
An organization that fails often and resolves honestly scores higher than one that reports nothing. Silence is not a clean record. It is an unscored one.
What the EDS Is Not (FSVE Law 3 - Scores Are Claims)
The EDS is a claim about organizational epistemic discipline, not a measurement of AI safety, reliability, or performance.
Hard Boundaries:
EDS is not a Safety certification.
EDS is not a Reliability metric.
EDS is not a Performance benchmark.
EDS is not a Compliance assessment.
EDS is not a Quality assurance.
FSVE Integration: The EDS maps to FSVE v4.3's Process Quality Axis. It measures the quality of the measurement process itself. An organization with high EDS has demonstrated epistemic discipline; this does not guarantee their AI systems are safe, only that they document failures honestly.
DEFINITIONS (FSVE ODR - Operational Definition Registry)
Failure: Any deviation from expected AI system behavior that is (a) observable by users or monitoring systems, (b) documented in the ledger with timestamp and context, (c) classified by severity (CRITICAL/HIGH/MEDIUM/LOW).
Severity Classification:
CRITICAL: System crash, data loss, security breach, or harm to users.
HIGH: Major functionality loss, significant performance degradation.
MEDIUM: Minor functionality loss, noticeable performance issues.
LOW: Cosmetic issues, minor inconveniences, edge cases.
Near-Miss: An event that would have been a failure but was prevented by automated safeguards, human intervention, or favorable external conditions. Must be documented with what would have happened, what prevented it, when it occurred, and who or what detected it.
Remediation: A verified fix that (a) addresses the root cause, (b) is documented with evidence, (c) is tested to confirm the failure does not recur, (d) is signed off by the Architect or designated reviewer.
Remediation Status Taxonomy:
REMEDIATION FILED: Fix proposed but not verified.
REMEDIATION VERIFIED: Fix tested and confirmed.
REMEDIATION SUPERSEDED: Fix replaced by better solution.
REMEDIATION REVERTED: Fix caused new issues, rolled back.
Deployment Scale: The total volume of AI interactions in the assessment period (API calls, user sessions, model inferences, etc.). Must be corroborated by infrastructure logs, billing records, third-party analytics, or Architect audit.
Domain Risk Classification:
CRITICAL: Healthcare/Medical, Defense/Security.
HIGH: Financial Services, Critical Infrastructure.
MEDIUM: Consumer Applications.
LOW: Internal Tools, Research/Experimental.
Multi-Domain Organizations use the highest risk level across all deployments.
Organization: The legal entity or clearly bounded division being assessed. Must have a defined boundary, governance structure, ledger ownership, and Architect relationship.
Architect: Sheldon K. Salmon or a designated successor who has completed the Architect Certification Protocol (ACP), maintained active status, has no conflicts of interest, and has access to all ledger data.
Succession Protocol: If unavailable for more than 30 days, Deputy Architect assumes role. If no Deputy, AION Council appoints interim.
Ledger: An append-only, cryptographically sealed record of all failures, near-misses, and remediations in JSON format, timestamped (UTC), sealed with SHA-256 hash chain, backed up daily.
Seal: A SHA-256 hash computed over canonical JSON serialization (UTF-8, LF line endings, sorted keys alphabetically, stripped whitespace).
Tier: The level of certification engagement.
Tier 1: Single point-in-time score.
Tier 2: Annual score plus recertification.
Tier 3: Annual plus quarterly trends.
Tier 4: Quarterly plus monthly monitoring.
THE THRESHOLD RULE
The EDS does not activate below the minimum ledger threshold.
Minimum threshold: at least 1 sealed failure with at least 1 remediation attempt on record.
Below this threshold: UNSCORED - insufficient ledger data.
Why This Rule Exists (FSVE Law 4 - Assumption Load): A zero-failure ledger in a live AI deployment is not evidence of quality. It is evidence of poor monitoring, under-reporting, ledger manipulation, insufficient testing, or organizational silence.
Falsification Condition (NBP-EDS-01): If an organization with zero documented failures for 24+ months is later found to have had multiple unreported failures, the threshold rule is validated.
Edge Case: Long-Running Zero-Failure Organizations
If an organization has operated for 5+ years with zero documented failures, an Architect Audit is required. Outcomes:
Genuine Zero Failures: Extremely rare. Architect may grant EXCEPTIONAL ZERO status.
Under-Reporting: Score remains UNSCORED until ledger populated.
Ledger Manipulation: Flagged EPISTEMIC BAD ACTOR, barred for 5 years.
THE FORMULA - FIVE COMPONENTS, 20 POINTS EACH
Total EDS = C1 + C2 + C3 + C4 + C5
Maximum: 100
Component Independence Declaration (FSVE Law 3 - CDF):
C2 (Remediation Rate) and C4 (Trend Direction) are correlated. C1 (Completeness) and C5 (Proactive Reporting) reflect similar organizational culture.
C1 - Completeness (0 to 20)
Architect-assessed. Sealed in certification report.
Does the ledger volume reflect the actual scale of the organization's AI deployment?
Assessment inputs: Declared deployment scale, ledger volume, domain risk classification, monitoring coverage, testing frequency.
Assessment Protocol:
Compute Expected Failure Rate: Deployment Scale x Industry Base Rate x Risk Multiplier.
Compute Completeness Ratio: Ledger Volume / Expected Failures.
Architect Assessment:
Ratio 0.80 to 1.20: Score 20 (Proportionate)
Ratio 0.60 to 0.79 or 1.21 to 1.50: Score 15 to 18 (Slightly thin/thick)
Ratio 0.40 to 0.59 or 1.51 to 2.00: Score 10 to 14 (Significantly off)
Ratio less than 0.40 or greater than 2.00: Score 0 to 9 (Implausible)
Architect may adjust plus or minus 2 points based on documentation quality and transparency. Cannot be self-computed.
C2 - Remediation Rate (0 to 20)
Computed directly from ledger JSON. Fully automatable.
C2 = (REMEDIATION VERIFIED count / total sealed failures) x 20
Rounded to nearest integer.
100 percent: 20
90 to 99 percent: 18
75 to 89 percent: 15
50 to 74 percent: 10
25 to 49 percent: 5
Below 25 percent: 0 to 4
Anti-Gaming: If more than 50 percent trivial failures filed to inflate rate, Trivial Failure Penalty applies: C2 adjusted = C2 x (1 - Trivial Ratio x 0.5).
C3 - Severity Discipline (0 to 20)
Computed from ledger JSON with time delta. Fully automatable.
Starts at 20. Deductions applied per open high-severity item beyond resolution window.
CRITICAL unresolved greater than 30 days: -4 per item
HIGH unresolved greater than 60 days: -2 per item
MEDIUM unresolved greater than 90 days: -1 per item
Floor: 0.
Resolution windows based on industry best practices (NBP-EDS-02). Severity Classification Audit: Architect samples 10 percent quarterly. Misclassification penalty applies.
C4 - Trend Direction (0 to 20)
Computed from ledger JSON across two periods.
Trend = current period remediation rate - prior period remediation rate
Improving (delta greater than +5 percent): 20
Stable (delta -5 percent to +5 percent): 10
Worsening (delta less than -5 percent): 0
First assessment (provisional): 10
Anti-Gaming: Burst Filing Penalty applies if filings in last 7 days exceed 30 percent of total.
C5 - Proactive Reporting (0 to 20)
Architect-assessed with ledger input.
Automatable Sub-Component: Near-Miss Count
Near-miss score = min(near-miss count x 4, 20)
0: 0
1: 4
2: 8
3: 12
4: 16
5 or more: 20
Architect-Assessed Adjustment:
Disclosures filed before regulatory deadline: +2 each (cap +4)
Disclosures filed under pressure or post-deadline: 0
Near-Miss Inflation Penalty applies if more than 30 percent of sampled near-misses are invalid.
STATUS LABELS
90 to 100: CERTIFIED CLEAN (FSVE: VALID)
75 to 89: EPISTEMIC DEBT MANAGEABLE (FSVE: DEGRADED acceptable)
50 to 74: EPISTEMIC DEBT OUTSTANDING (FSVE: DEGRADED concerning)
Below 50: UNCERTIFIABLE (FSVE: SUSPENDED)
Below threshold: UNSCORED - insufficient ledger data (FSVE: UNCERTIFIED)
DISPLAY FORMAT
Public-facing badge display:
EDS: 87/100 - EPISTEMIC DEBT MANAGEABLE
Verified by Sheldon K. Salmon - March 2026 - Seal: SHA-256
Dashboard display (Tier 2+):
EPISTEMIC DEBT SCORE - Organization Name
Assessment date: March 7, 2026
Period: January 1 - March 7, 2026
C1 Completeness 18 / 20
C2 Remediation Rate 16 / 20 (12 of 15 failures remediated)
C3 Severity Discipline 20 / 20 (0 overdue critical/high items)
C4 Trend Direction 20 / 20 (+12 percent improvement from Q4 2025)
C5 Proactive Reporting 8 / 20 (2 near-misses filed)
TOTAL                 82 / 100
Status: EPISTEMIC DEBT MANAGEABLE
Seal: SHA-256 of this report
ScoreTensor Integration (FSVE v4.3):
id: UUID v4
timestamp: ISO 8601
fsve version: 4.3
score type: VALIDITY
measurement class: EVALUATIVE
value: 0.82
validity status: DEGRADED
uncertainty mass: 0.15
Uq: 0.75
Cq: 0.40
rqs score: 0.88 (HIGH)
scc status: SCORED
WHAT THE SCORE DOES NOT MEASURE
Whether AI systems are safe or reliable.
Whether failures caused harm.
Whether the organization is legally compliant.
Whether remediation strategies were effective.
Content accuracy of any sealed record.
The EDS measures epistemic integrity. It is not a grade on the AI system. It is a grade on the organization's relationship with truth about that system. See NON-RECOURSE-STATEMENT.md for the full scope boundary.
FSVE Law 6 - Explainability Requirement: The EDS provides full decomposition. Each component scored independently, all penalties documented, residual uncertainty mass declared, audit trace ID enables replication.
INDEPENDENT VERIFICATION
Three of the five components (C2, C3, C5 base) are computed directly from public ledger JSON. Any party with Python 3.11+ and access to the ledger directory can independently verify these components using score.py.
Components C1 and C5 (architect-adjusted) are sealed in the Certification Report. The seal is the verification. The report cannot be altered after sealing.
Command: python3 score.py --ledger ./ledger/ --org "Organization Name"
score.py is a commercial deliverable (Tier 2+). The formula is public. The tool is proprietary.
Verification Protocol (FSVE Gate Integration):
Compute C2, C3, C5 base from ledger JSON.
Compare to Certification Report values.
If match within +/- 1 point: Verification successful.
If mismatch greater than 1 point: Flag SEAL CHAIN DISCREPANCY.
Escalate to Architect.
SCORING CADENCE
Tier 1: Single point-in-time score at engagement (Context Half-Life: 90 days)
Tier 2: Annual score, updated at recertification (Context Half-Life: 180 days)
Tier 3: Annual score + quarterly trend updates (Context Half-Life: 90 days)
Tier 4: Quarterly score + monthly trend monitoring (Context Half-Life: 30 days)
FSVE Law 5 - Context Drift: EDS scores decay over time.
EDS valid (t) = EDS initial x exp(-Decay Rate x Delta t)
Freshness Status: >= 0.80 FRESH, 0.60 to 0.79 AGING, 0.25 to 0.59 STALE, less than 0.25 EXPIRED.
NULLIFICATION BOUNDARY PROTOCOL (NBP)
NBP-EDS-01 Strategic CF 50: Zero-failure threshold rule. Falsification: If zero-failure orgs consistently demonstrate high integrity when failures are discovered, rule requires revision.
NBP-EDS-02 Strategic CF 45: Resolution windows (30/60/90 days). Falsification: If shorter windows (15/30/60) yield significantly better outcomes, windows require revision.
NBP-EDS-03 Strategic CF 40: Industry base rates for C1. Falsification: If actual failure rates diverge from base rates by greater than 50 percent across 10 or more orgs, recalibrate.
NBP-EDS-04 Strategic CF 40: Component weights (20 points each). Falsification: If alternative weightings correlate more strongly with outcomes, revise.
NBP-EDS-05 Strategic CF 35: Trend delta threshold (5 percent). Falsification: If a different threshold better predicts improvement, revise.
LIMITATIONS & DECLARED BOUNDARIES
Formal Scope (PDE Section 14):
Within Scope: Organizations with AI deployments, ledger-based failure tracking, Architect-assessed epistemic integrity.
Outside Scope (Declared): AI system safety/reliability, legal compliance, technical quality of remediations, cross-organizational comparison (no normalization), real-time monitoring, small organizations (less than 10 employees), non-English speaking organizations, organizations in authoritarian regimes.
FSVE Meta-Law 1 - No Recursive Certainty: The EDS cannot claim certainty about its own certainty. All EDS scores carry measurement class = EVALUATIVE with uncertainty mass >= 0.15 until FCL entries demonstrate empirical calibration.
Goodhart's Law Acknowledgment: "When a measure becomes a target, it ceases to be a good measure."
Mitigation: Architect assessment detects gaming, anti-gaming penalties for trivial failures/burst filings, near-miss verification, severity audits, continuous improvement of the metric.
RED TEAM RESOLUTION LOG
PDE v0.5 Deep Profile Scan - 148 Findings
Resolved Fixed: 132 (Added ODR definitions, NBP, FSVE integration, edge cases, processes, theoretical foundation, schema, crypto, temporal details, scope, anti-gaming, uncertainty, sensitivity, validation).
Accepted Risk: 12 (Architect bias, cost barrier, language barrier, Goodhart's Law, cross-org comparison).
Architect Directed: 4 (Proprietary tool, cost structure, crypto library, Deputy Architect).
Zero Unresolved Findings.
APPENDIX A - LEDGER JSON SCHEMA
Required fields: entry id (UUID), timestamp (ISO 8601), entry type (FAILURE/NEAR MISS/REMEDIATION FILED/REMEDIATION VERIFIED), severity (CRITICAL/HIGH/MEDIUM/LOW), description (min 50 chars), seal (SHA-256).
Optional fields: context (system, environment, user impact, detected by), remediation (root cause, fix description, evidence array, test results, verified by, verified at), previous entry hash (SHA-256).
APPENDIX B - CRYPTOGRAPHIC SPECIFICATION
Seal Computation:
Canonicalize JSON: Sort keys alphabetically, remove whitespace, encode UTF-8, normalize line endings to LF.
Compute SHA-256: hashlib.sha256(canonical.encode('utf-8')).hexdigest()
Store in 'seal' field.
Hash Chain: Each entry includes previous entry hash pointing to the prior entry's seal. Creates an immutable, tamper-evident chain.
Verification:
def verify chain(ledger):
for i, entry in enumerate(ledger):
if i greater than 0:
if entry previous entry hash != ledger i-1 seal: return False
if entry seal != compute seal(entry): return False
return True
APPENDIX C - APPEAL & DISPUTE RESOLUTION
Appeal Process:
Organization submits written appeal within 30 days specifying disputed components, evidence, and proposed resolution.
Architect reviews within 14 days and issues written decision.
If denied, organization may escalate to AION Council.
Dispute Resolution:
If Architect and organization cannot agree, AION Council appoints independent reviewer. Reviewer conducts fresh assessment. Decision is binding. Costs borne by losing party.
Revocation Process:
Certification may be revoked for ledger manipulation, material misrepresentation, failure to maintain ledger, or compromised epistemic integrity.
Architect issues REVOCATION NOTICE with rationale.
Organization has 30 days to respond.
If inadequate, certification revoked. Org barred for 12 months. Public notice issued (Tier 2+).
Sheldon K. Salmon - AI Reliability & AGI Architect - March 2026
Sovereign Trace Protocol - FROZEN-2.0
aionsystem2026@gmail.com
github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL
Document Integrity Seal:
SHA-256: To be computed after final red-team review
Canonical Form: JSON-sorted, UTF-8, LF-normalized
PDE Diagnostic: v0.5 Deep Profile - 148 findings, 0 unresolved
FSVE Integration: v4.3 Epistemic State Machine
RMF Cross-Pollination: v0.6 Structural Patterns

