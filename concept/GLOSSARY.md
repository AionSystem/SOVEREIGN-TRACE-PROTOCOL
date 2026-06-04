# GLOSSARY — Sovereign Trace Protocol

**Plain-language definitions for all terms used in this repository.**
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Updated:** June 2026

This glossary translates the technical and architectural vocabulary of the
Sovereign Trace Protocol into plain language. Terms are grouped by category.
If you are reading the concept specifications and encounter an unfamiliar term,
start here.

---

## CORE PROTOCOL TERMS

**Sovereign Trace Protocol (STP)**
The full name of this project. A personal infrastructure for sealing
significant moments with a permanent, cryptographic triple-time stamp.
"Sovereign" means the individual holds the key — no platform, no audience,
no institution required. "Trace" from Latin *trahere* — to draw, to pull,
to leave a mark.

**Trace Entry**
The text you write before sealing. One micro-entry describing exact
present-moment observations, actions, or facts. No narrative. No "what this
means." Just what happened, as precisely as you can state it.

**Triple-Time Seal**
The cryptographic output. A SHA-256 hash that permanently binds your trace
entry to three simultaneous calendar representations of the moment you sealed
it: Gregorian, Hebrew lunisolar, and 13 Moon Dreamspell. Altering the text
or any date field breaks the seal. That breakage is the integrity proof.

**SHA-256**
The cryptographic algorithm used to generate the seal. An industry-standard
one-way hash function — given the same input, it always produces the same
64-character output. Change one character of the input and the output changes
completely. Used in Bitcoin, TLS, and most secure systems worldwide. Part of
Python's standard library — no external dependencies required.

**Seal**
The 64-character hexadecimal output of SHA-256 applied to your trace entry
plus all three calendar representations. It is the proof. Store it alongside
your entry. If the seal matches on verify — the entry is intact. If it
doesn't — something was altered after sealing.

**Verify**
The `verify()` function in `sovereign_trace_stamp.py`. Pass it the original
entry text and a SovereignStamp object. Returns `True` if the entry is
unchanged. Returns `False` if anything was altered. Single-character tamper
detection.

**Temporal Sovereignty**
The condition in which your record of a moment cannot be altered by any
external party after it is sealed. The stamp belongs to the moment.
No platform can edit it, no vendor can delete it, no outage can change it.

**Epistemic Debt**
What accumulates when AI systems generate claims that are not captured,
logged, or verified. When those claims propagate into decisions and later
fail, the debt pays out — often expensively. The STP creates the
infrastructure to track and remediate epistemic debt systematically.

---

## CALENDAR SYSTEMS

**Gregorian Calendar**
The internationally standard civic calendar. January 1 year 1 CE.
The calendar of governments, contracts, and infrastructure. Used as the
reference anchor in the triple-time seal.

**Hebrew Lunisolar Calendar**
A calendar system combining lunar months with solar year correction.
Year 1 corresponds to approximately 3760 BCE on the Gregorian calendar.
The current year (2026 CE) is 5786 in the Hebrew count. The calendar has
complex postponement rules (dehiyot) that prevent certain holy days from
falling on prohibited weekdays. The STP implements all four postponement
rules correctly — a detail that many implementations get wrong.

**Dehiyot**
The four postponement rules of the Hebrew calendar that determine when
Rosh Hashanah (the New Year) actually begins. The rules are:
*Lo ADU Rosh* (not on Sunday, Wednesday, or Friday), *Molad Zaken*
(if the new moon falls too late in the day), *GaTaRaD*, and
*BeTUTeKaPoT* (both check adjacent year lengths for structural anomalies).
FROZEN-1.0 was retired specifically because it omitted GaTaRaD and
BeTUTeKaPoT. FROZEN-4.0 implements all four correctly.

**Civil-Day Convention**
The rule used to assign a Hebrew date to a Gregorian calendar date.
Hebrew days technically begin at sunset. The civil-day convention assigns
the Hebrew date corresponding to the daytime hours of a civil date —
matching the output of authoritative converters Hebcal.com and Chabad.org.
Example: Rosh Hashanah 5786 begins at sundown September 22, 2025, but the
civil-day convention assigns September 23, 2025 = 1 Tishri 5786.

**13 Moon Dreamspell Calendar**
A rhythmic calendar system proposed by José Argüelles. 13 months of 28 days
each = 364 days, plus one "Day Out of Time" (July 25). The year begins
July 26. Each of the 13 months has a name: Magnetic, Lunar, Electric,
Self-Existing, Overtone, Rhythmic, Resonant, Galactic, Solar, Planetary,
Spectral, Crystal, Cosmic. The STP uses this system as its third
civilizational time anchor.

**Day Out of Time**
July 25 in the Dreamspell calendar. The 365th day of the solar year,
outside the 13 × 28 structure. The `_dreamspell()` function returns
`"Day Out of Time"` for July 25 of any year.

---

## CODE TERMS

**FROZEN-4.0**
The current canonical version of `sovereign_trace_stamp.py`. "FROZEN"
means the file is written once, verified once, deployed permanently.
No patches. No updates. If a defect is found, the file is retired and a
new version is built from scratch. The version number increments with each
new creation. "4.0" because earlier frozen versions (1.0, 2.0, 3.0) have
been retired with documented defects.

**FROZEN-3.0 (Retired)**
Retired due to incorrect self‑test anchor data (RH 5787 and Erev RH 5787).
Algorithm was correct; test data was not. No stamp produced by FROZEN-3.0
carries a cryptographic error. Retired to maintain the frozen discipline.
Archived in `stamp/FROZEN-3.0-RETIRED/`.

**FROZEN-2.0 (Retired)**
Retired due to eight defects including no NFC normalization, no version
field in seal, pre‑reform boundary slip, and unbounded Hebrew year loop.
Archived in `stamp/FROZEN-2.0-RETIRED/`.

**FROZEN-1.0 (Retired)**
The first version of the stamp function. Retired March 3, 2026 —
same session it was created — after the dehiyot defect was discovered.
Archived in `stamp/FROZEN-1.0-RETIRED/`. All stamps produced by
FROZEN-1.0 carry a known Hebrew field error (off by one day for all
5786 dates). Do not use.

**SovereignStamp**
The Python class returned by the `stamp()` function. An immutable object
holding five fields: `gregorian`, `hebrew`, `dreamspell`, `unix_utc`,
and `seal`. Immutable means attempting to set any attribute after creation
raises an `AttributeError`. Frozen by design.

**stdlib only**
The stamp function uses exclusively Python's standard library — `hashlib`,
`json`, and `datetime`. No third-party packages required. No `pip install`.
No dependency rot. Run it anywhere Python 3.11+ is installed.

**Self-test**
Run `python sovereign_trace_stamp.py --test` to execute 82 built-in
verification checks against known anchor values. Any failure means a
calendar algorithm was broken — do not deploy until all tests pass.
The self-test is the integrity gate for the frozen deployment.

**Anchor Seal**
The specific seal produced for the origin trace entry at the session of
creation (March 3, 2026). It is the cryptographic birth record of the
protocol. Reproducible only with FROZEN-4.0 code. Documented in
`stamp/FROZEN-4.0-MANIFEST.md`.

---

## ISSUE TEMPLATE TERMS (v4.0)

**Issue Templates**
The 31 YAML files in `.github/ISSUE_TEMPLATE/` that users fill out to submit
a trace, audit request, or other sealed record. Each template enforces
GitHub‑compliant fields, size limits, and legal declarations. No blank
issues allowed.

**General Feedback (Template 00)**
A catch‑all template for suggestions, bug reports, or proposing new templates.
This template does **not** create a sealed record. It is a channel for
community input.

**Prompt Seal (Template 15)**
A template for sealing the exact prompt text before deploying it to a
production AI system. Proves what was authorized, at what time, and by whom.

**Dataset Declaration (Template 17)**
A template for sealing a dataset checksum and description before training
begins. Prevents after‑the‑fact claims about what data was used.

**AI Output Sample (Template 22)**
A template for sealing a representative sample of AI outputs for periodic
auditing. Allows longitudinal tracking without a full certification engagement.

**Bias Audit Record (Template 23)**
A template for sealing the results of an AI bias or fairness audit.
Proves that disparity was measured before deployment.

**Red Team Engagement (Template 24)**
A template for sealing the scope, methodology, and rules of engagement for a
red team exercise before it begins. Proves what was authorized to test.

**Model Card Seal (Template 25)**
A template for sealing a model card or system card at the time of publication.
Proves that documented capabilities and limitations existed before deployment.

**Human Oversight Log (Template 26)**
A template for sealing a record of human review and override of an AI output.
Proves human judgment was exercised before action was taken.

**Code Snippet Seal (Template 27)**
A template for sealing a small code snippet, function, or algorithm.
Proves prior art before sharing publicly.

**Research Logbook (Template 28)**
A template for sealing daily research notes, experiment results, or lab
observations. Proves what was observed and when.

**Identity Anchor (Template 29)**
A template for sealing a public key fingerprint, email, or social media handle
to your GitHub identity. Proves you control both.

**Temporal Commitment (Template 30)**
A template for sealing a personal or professional commitment with a deadline.
Proves what you pledged and when.

---

## ABUSE DETECTION TERMS (v4.0)

**Abuse Detector**
A GitHub Action workflow (`abuse-detector.yml`) that scans every newly opened
issue for prohibited content (threats, CSAM, doxing, credential leaks).
Runs before any seal is created. Prevents illegal content from ever reaching
the immutable ledger.

**Tiered Scoring**
The abuse detector uses three tiers:
- **Green** (score < 0.4): passes through normally.
- **Yellow** (score 0.4–0.7): adds a `needs-review` label, posts a warning
  comment, but does not close the issue. Human review required.
- **Red** (score > 0.7): automatically closes and locks the issue, logs the
  abuse, and tracks repeat offenders.

**Repeat Offender**
A GitHub user who accumulates three or more red‑tier violations. Their
subsequent issues are automatically rejected without scoring.

**Appeal**
A user who believes their issue was incorrectly rejected can email
`aionsystem@outlook.com` with the issue number. Only the Architect can
reopen a closed‑red issue.

**Perspective API (optional)**
Google's toxicity detection API. Used to score the text of the issue
for hostility, threats, or harassment. If enabled, it contributes to
the final abuse score. Can be disabled by not providing the API key.

---

## BLOCKCHAIN ANCHOR TERMS (v4.0)

**Blockchain Anchor**
A script (`stp_blockchain_anchor.py`) that periodically takes all new STP
seals from the past week, computes a Merkle root of their SHA‑256 hashes,
and posts that root to one or more public blockchains. This provides
decentralized, permanent proof of the batch of seals.

**Merkle Root**
A single 64‑character hash that summarizes a list of many individual hashes.
If any individual seal changes, the Merkle root changes. Used to anchor
thousands of seals with a single blockchain transaction.

**Bitcoin Anchor**
Posts the Merkle root as an `OP_RETURN` output in a Bitcoin transaction.
`OP_RETURN` is a provably unspendable output that can store up to 80 bytes
of arbitrary data. Permanent, immutable, and visible on the Bitcoin ledger.

**Hedera Consensus Service (HCS)**
A service on the Hedera network that provides fast, fair, and low‑cost
consensus ordering of messages. The STP anchor posts the Merkle root as a
topic message. HCS is more energy‑efficient than Bitcoin and costs pennies.

**Ethereum Anchor**
Posts the Merkle root as a transaction to a smart contract (or as a raw
transaction with the root in the input data). Ethereum gas fees apply.

**Stellar Anchor (optional)**
Posts the Merkle root as a text memo on a zero‑value transaction.
Stellar fees are extremely low (0.00001 XLM). Optional because Stellar's
mainnet usage is less common than Bitcoin/Ethereum.

---

## ENTERPRISE AND CERTIFICATION TERMS

**Enterprise Deployment**
Use of the Sovereign Trace Protocol by an organization to log, seal,
and maintain an immutable audit trail of AI system failures, investigations,
and remediations. Enterprise deployment requires a commercial license
and is eligible for certification under the six‑tier system (Tiers 0–5).

**Epistemic Debt (Organizational)**
The accumulated gap between what an organization's AI systems have claimed
and what can be verified, corrected, or accounted for. Epistemic debt
grows silently when AI outputs are not logged. It pays out when a
regulator, client, or court asks "when did you know, and what did you do?"
The Sovereign Trace Protocol creates the infrastructure to track and
retire epistemic debt systematically.

**AI Audit Trail**
The organizational equivalent of a personal trace ledger. A permanent,
immutable record of AI failure events, the investigations that followed,
and the remediations applied. Sealed with FROZEN-4.0 stamps at each entry.
Cannot be edited after sealing — only appended.

**Remediation Record**
An entry appended to an existing failure record documenting what was done
to address the failure. The original failure entry is not deleted or
modified. Both entries — failure and remediation — are permanent.
The combination constitutes a complete epistemic record.

**Epistemic Debt Score (EDS)**
A 0–100 metric measuring an organization's AI epistemic integrity across
five components: Completeness, Remediation Rate, Severity Discipline,
Trend Direction, and Proactive Reporting. The formula is public in
`EPISTEMIC-DEBT-SCORE.md`.

**Trust Registry**
The public, immutable, STP‑sealed list of all active certifications
(enterprise tiers Tiers 0–5 and personal tracks SACS/CAPC). Stored on the
STP ledger as a set of entries. Anyone can query a registry entry ID to
check status, expiry, and revocation.

**Sovereign AI Constitution Compliance (SACS)**
A lightweight personal certification for individuals running their own AI
with THE CONSTITUTION v2.1 embedded. $49 one‑time or $12/year.
Badge: crimson and gold variant of the Constitutional Compliance badge.

**Constitutional AI Practitioner Credential (CAPC)**
A professional certification for individuals who build AI systems for others
or deploy AI in public‑facing contexts. $199/year, identity‑verified,
optional background check. Badge: silver and blue shield.

**AION-Registry**
The public certification registry operated under this protocol.
Lists organizations by certification tier, certification date, and
outcome (valid / expired / revoked). Entries are permanent — subject
to the No‑Deletion Policy. The registry is the source of truth for
Sovereign Certified status.

**Sovereign Certified**
The mark issued to organizations that have passed a formal certification
audit under the Tier 1–5 process. Use of this mark requires a current,
executed commercial license agreement. See `CERTIFICATION.md`
and `TRADEMARK-USAGE-POLICY.md`.

**No-Deletion Policy**
The architectural and legal commitment that public registry entries,
certification outcomes, and filed incident records are permanent.
This policy is documented in `POLICIES.md` (planned) and referenced
in `DATA-PROCESSING-AGREEMENT.md`. It is the organizational expression
of the same principle that makes FROZEN-4.0 immutable — permanence
is not a feature, it is the architecture.

**Triple License**
The three‑tier license structure of this repository: Apache 2.0 for
individual and non‑commercial use, GPL v3 copyleft for modified
distributions, and a commercial license for white‑label, SaaS, and
certification services. See `LICENSE-EXPLANATION.md` for plain‑language
guidance on which applies to your situation.

---

## ARCHITECTURE TERMS (preserved from original, updated versions)

**AION Constitutional Stack**
The broader framework architecture built by Sheldon K. Salmon.
The Sovereign Trace Protocol is one product built within this stack.
Other components include FSVE (certainty scoring), CAL (code governance),
FA (function design), and others. Primary repository: AionSystem/AION-BRAIN.

**AION-BRAIN**
The private origin repository where the Sovereign Trace Protocol was
first conceived and documented (March 3, 2026). Contains 2040+ files,
60+ frameworks, and 75+ validated entries. The STP concept specifications
in `concept/` originate from AION-BRAIN session documents.

**M-NASCENT**
Convergence state designation. Means: the concept is specified and
deployed but has zero confirmed validation entries (FCL entries).
The architecture is sound. The proof is not yet accumulated.
Contrasts with M-MODERATE (some validation) and M-STRONG
(statistically significant validation). STP v4.0 is M-NASCENT.

**FCL Entry**
Falsification/Confirmation Log entry. A documented instance that either
confirms or challenges a framework's core claim under real conditions.
The STP currently has 0 confirmed FCL entries — it has not yet been
tested with real users in production conditions.

**DDL Field (Design Declaration Layer)**
A structured metadata header used in AION-BRAIN specifications.
It declares the framework name, origin, stack position, convergence
state, active layers, co-authors, and PIE root. Appears at the top of
the concept specification documents in `concept/`.

**PIE Root**
Proto-Indo-European etymological root. A linguistic anchor tracing a
concept to its oldest recoverable word origin. Used in AION-BRAIN
specifications as a grounding mechanism — the root constrains what
the term can legitimately mean. For Sovereign Trace Protocol:
*trahere* (to draw, to pull, to leave a trace).

**Significance Hunger**
The phrase used in the concept specifications to describe the
psychological need for recognition of one's own significance.
The STP's core claim is that this need resolves at the moment of
permanent registration — not at the moment of audience acknowledgment.
This is the untested core hypothesis of the protocol (tagged `[?]`
in specification documents).

---

## LEGAL TERMS (unchanged from original, dates updated)

**Defensive Publication**
A public disclosure of an inventive concept made specifically to establish
prior art and prevent others from patenting the concept. Unlike a patent,
it grants no exclusive rights — but it permanently prevents anyone else
from obtaining a patent on the disclosed concept. The STP's `PATENTS.md`
is a defensive publication.

**Common Law Trademark**
Trademark rights that arise from actual use of a mark in commerce,
without registration. Enforceable under 15 U.S.C. § 1125(a) (Lanham
Act) but weaker than a registered trademark. The STP holds common law
rights in "Sovereign Trace Protocol," "Sovereign Certified," and
related marks. USPTO registration is pending first commercial revenue.

**Triple License**
The three‑tier license structure of this repository. Apache 2.0 for
individual and non‑commercial use. GPL v3 copyleft for modified
distributions — corporate forks cannot be hidden in proprietary code.
Commercial license required for white‑label use, SaaS offerings, and
certification services. See `LICENSE`, `LICENSE-COMMERCIAL.md`.

**Copyleft**
A licensing condition (used in GPL v3) that requires any distributed
modification of the software to also be released under the same open
source license. If a company forks this code, modifies it, and ships
it as a product — they must open-source their modifications. This is
the "viral" property of GPL that prevents corporate appropriation
of open source work.

**FROZEN Declaration (legal sense)**
The architectural commitment that `sovereign_trace_stamp.py` will never
be modified after deployment. In legal terms, this is significant because
it means all stamps produced by FROZEN-4.0 carry the same integrity
guarantee — the code that produced them cannot have been silently altered.
It is the technical basis for the permanence claim.

---

*GLOSSARY — Sovereign Trace Protocol*
*Author: Sheldon K. Salmon | June 2026*
*This document is updated as new terms are introduced.*
*Plain language first. Precision throughout.*
