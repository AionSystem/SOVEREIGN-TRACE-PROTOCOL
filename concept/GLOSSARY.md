# GLOSSARY — Sovereign Trace Protocol

**Plain-language definitions for all terms used in this repository.**
**Author:** Sheldon K. Salmon — AI Reliability & ADI Architect
**Updated:** March 2026

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
BeTUTeKaPoT. FROZEN-2.0 implements all four correctly.

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

**FROZEN-2.0**
The current canonical version of `sovereign_trace_stamp.py`. "FROZEN"
means the file is written once, verified once, deployed permanently.
No patches. No updates. If a defect is found, the file is retired and a
new version is built from scratch. The version number increments with each
new creation. "2.0" because FROZEN-1.0 was retired due to the Hebrew
calendar defect.

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
Run `python sovereign_trace_stamp.py --test` to execute 35 built-in
verification checks against known anchor values. Any failure means a
calendar algorithm was broken — do not deploy until all tests pass.
The self-test is the integrity gate for the frozen deployment.

**Anchor Seal**
The specific seal produced for the origin trace entry at the session of
creation (March 3, 2026). It is the cryptographic birth record of the
protocol. Reproducible only with FROZEN-2.0 code. Documented in
`stamp/FROZEN-2.0-MANIFEST.md`.

---

## ARCHITECTURE TERMS

**AION Constitutional Stack**
The broader framework architecture built by Sheldon K. Salmon.
The Sovereign Trace Protocol is one product built within this stack.
Other components include FSVE (certainty scoring), LAV (linguistic
validation), TOPOS (persistent shape architecture), and others.
Primary repository: AionSystem/AION-BRAIN.

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
(statistically significant validation).

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

**DUAL-HELIX v2.0**
A build and deep-thinking methodology used to develop frameworks and
concepts within the AION Constitutional Stack. The concept specifications
in `concept/` were produced using DUAL-HELIX. It is an internal tool —
its mechanics are not required to understand or use the STP.

**TOPOS v0.3**
A framework within the AION stack for mapping the persistent shape of
AI systems — the invariant structure between frozen weights and fluid
outputs. Referenced in concept specifications as the theoretical
foundation for why "frozen code = frozen stamp." Internal tool.

**CPA-001**
Contextual Protocol Assessment. A harm evaluation methodology used
in AION-BRAIN to classify a build's risk tier and bias exposure.
The STP is classified as Harm Tier 2 (low direct harm ceiling).
Internal methodology — not required to use the STP.

**Significance Hunger**
The phrase used in the concept specifications to describe the
psychological need for recognition of one's own significance.
The STP's core claim is that this need resolves at the moment of
permanent registration — not at the moment of audience acknowledgment.
This is the untested core hypothesis of the protocol (tagged `[?]`
in specification documents).

---

## LEGAL TERMS

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
The three-tier license structure of this repository. Apache 2.0 for
individual and non-commercial use. GPL v3 copyleft for modified
distributions — corporate forks cannot be hidden in proprietary code.
Commercial license required for white-label use, SaaS offerings, and
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
it means all stamps produced by FROZEN-2.0 carry the same integrity
guarantee — the code that produced them cannot have been silently altered.
It is the technical basis for the permanence claim.

---

*GLOSSARY — Sovereign Trace Protocol*
*Author: Sheldon K. Salmon | March 2026*
*This document is updated as new terms are introduced.*
*Plain language first. Precision throughout.*

---

## ENTERPRISE AND CERTIFICATION TERMS

**Enterprise Deployment**
Use of the Sovereign Trace Protocol by an organization to log, seal,
and maintain an immutable audit trail of AI system failures, investigations,
and remediations. Enterprise deployment requires a commercial license
and is eligible for certification under the three-tier system.

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
and the remediations applied. Sealed with FROZEN-2.0 stamps at each entry.
Cannot be edited after sealing — only appended.

**Remediation Record**
An entry appended to an existing failure record documenting what was done
to address the failure. The original failure entry is not deleted or
modified. Both entries — failure and remediation — are permanent.
The combination constitutes a complete epistemic record.

**Epistemic Debt Statement**
A written assessment issued under Tier 3 certification. Documents the
organization's full AI audit record: failures logged, remediations
completed, outstanding debt, and trend direction. A summary version
is published to the AION-Registry.

**AION-Registry**
The public certification registry operated under this protocol.
Lists organizations by certification tier, certification date, and
outcome (verified / deficient). Entries are permanent — subject to
the No-Deletion Policy. The registry is the source of truth for
Sovereign Certified status.

**Sovereign Certified**
The mark issued to organizations that have passed a formal certification
audit under the Tier 2 or Tier 3 process. Use of this mark requires a
current, executed commercial license agreement. See `CERTIFICATION.md`
and `TRADEMARK-USAGE-POLICY.md`.

**No-Deletion Policy**
The architectural and legal commitment that public registry entries,
certification outcomes, and filed incident records are permanent.
This policy is documented in `POLICIES.md` (planned) and referenced
in `DATA-PROCESSING-AGREEMENT.md`. It is the organizational expression
of the same principle that makes FROZEN-2.0 immutable — permanence
is not a feature, it is the architecture.

**FCL-ST-001**
The first staged Falsification/Confirmation Log candidate for the
Sovereign Trace Protocol: the first user who reports resolution of
significance hunger from the stamp alone, without any resonance
from another person. This is the most important early data point —
it either confirms or challenges the protocol's core hypothesis.

**Triple License**
The three-tier license structure of this repository: Apache 2.0 for
open use, GPL v3 copyleft for modified distributions, and a
commercial license for enterprise and certification use.
See `LICENSE-EXPLANATION.md` for plain-language guidance on which
applies to your situation.
