# PATENTS.md — Defensive Publication & Prior Art Record

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Date of first disclosure:** March 3, 2026
**Repository:** AionSystem/SOVEREIGN-TRACE-PROTOCOL
**Origin archive:** AionSystem/AION-BRAIN

---

## PURPOSE OF THIS DOCUMENT

This document constitutes a **defensive publication** — a formal public
disclosure of inventive concepts originated in the Sovereign Trace Protocol.
Its purpose is to establish prior art under 35 U.S.C. § 102 (United States),
European Patent Convention Article 54, and equivalent provisions in all
jurisdictions that recognize prior art through public disclosure.

A defensive publication does not create patent rights in the author.
It creates a public prior art record that prevents any other party from
subsequently patenting the disclosed concepts and asserting those patents
against users of this open source software.

**Intent:** This software is and shall remain open. These disclosures
are made to keep it that way.

---

## DEFENSIVE PUBLICATION 001 — TRIPLE-TIME CRYPTOGRAPHIC SEAL

**Title:** Method for Binding Textual Content to Simultaneous
Multi-Civilizational Calendar Representations via Cryptographic Hash

**First disclosed:** March 3, 2026 — AionSystem/AION-BRAIN (private archive)
**First public disclosure:** March 2026 — AionSystem/SOVEREIGN-TRACE-PROTOCOL

**Concept:**

A method of generating a cryptographic seal (SHA-256 or equivalent hash)
that binds:

1. A textual entry (the "trace"), to
2. A Gregorian calendar representation of the moment of generation, and
3. A Hebrew lunisolar calendar representation of the same moment,
   computed using the full four dehiyot postponement rules
   (Lo ADU Rosh, Molad Zaken, GaTaRaD, BeTUTeKaPoT) and
   civil-day epoch convention, and
4. A 13 Moon Dreamspell calendar representation of the same moment,
   computed from the July 26 year-start convention with
   Day Out of Time handling,

such that alteration of the textual entry or any calendar field
causes the seal to fail verification, providing cryptographic
proof of the exact temporal moment of inscription across
three distinct civilizational frameworks simultaneously.

**Implementation:**

The JSON payload fed to the hash function is deterministically sorted
by key (sort_keys=True) and serialized with compact separators, ensuring
reproducibility across implementations, platforms, and language versions.

**Prior art record (reproducible):**

```
Entry:       "Origin trace — Sovereign Trace Protocol FROZEN-2.0 sealed at session of birth."
Gregorian:   March 3, 2026
Hebrew:      14 Adar 5786
Dreamspell:  Day 25, Galactic Moon 8/13
Unix UTC:    1741021200
Seal:        19276f3fbdd02960ffab7eb9ed044e023cb68ffc426179c71cb1476d07d477e2
```

This seal is reproducible using `stamp/sovereign_trace_stamp.py` (FROZEN-2.0)
in this repository. Reproducibility is the prior art verification mechanism.

---

## DEFENSIVE PUBLICATION 002 — FROZEN CODE DESIGNATION

**Title:** Method for Designating Software as Permanently Immutable
Post-Verification with Structured Retirement Protocol

**First disclosed:** March 3, 2026 — AionSystem/SOVEREIGN-TRACE-PROTOCOL

**Concept:**

A software deployment methodology wherein:

1. A module is designated FROZEN upon first verified deployment,
2. No modifications, patches, or updates are made to the frozen module
   under any circumstances after designation,
3. If a defect is discovered, the frozen module is retired to an
   archived directory with a documented defect record,
4. A new module is created from first principles (not by patching)
   and subjected to full verification before receiving the next
   FROZEN designation,
5. The designation carries a version number (e.g., FROZEN-2.0) that
   increments with each new creation from first principles,
6. All outputs produced by a frozen module carry implicit provenance
   tied to that version designation.

**Prior art record:** FROZEN-2.0 designation applied to
`stamp/sovereign_trace_stamp.py` on March 3, 2026 in this repository.
FROZEN-1.0 retirement record is documented in
`stamp/FROZEN-1.0-RETIRED/ARCHIVE-EMPTY.md`.

---

## DEFENSIVE PUBLICATION 003 — SIGNIFICANCE HUNGER RESOLUTION INFRASTRUCTURE

**Title:** Personal Significance Registration System Using
Multi-Calendar Cryptographic Timestamps as Primary Resolution Mechanism

**First disclosed:** March 3, 2026 — AionSystem/AION-BRAIN,
SOVEREIGN-TRACE-v0.1-SPEC.md and SOVEREIGN-TRACE-v0.2-SPEC.md

**Concept:**

A personal infrastructure system wherein:

1. An individual records exact present-moment observations without
   narrative interpretation (the "trace entry"),
2. The entry is sealed with a multi-calendar cryptographic timestamp
   at the moment of recording,
3. The act of sealing — not the act of publication or reception
   by another party — constitutes the primary satisfaction of
   the psychological need for recognition of personal significance,
4. No social metrics, view counts, or audience acknowledgment
   mechanisms are required or displayed,
5. Optional resonance signatures may be collected but are not
   aggregated, counted, or displayed in any numerical form.

**Prior art record:** SOVEREIGN-TRACE-v0.2-SPEC.md, March 3, 2026,
AionSystem/SOVEREIGN-TRACE-PROTOCOL.

---

## PATENT INTENT NOTICE

The author, Sheldon K. Salmon, intends to file a Provisional Patent
Application (PPA) with the United States Patent and Trademark Office
upon receipt of first commercial revenue from services associated with
this protocol. Filing a PPA within 12 months of this public disclosure
preserves the ability to seek patent rights while maintaining the
open source nature of the code under the Apache 2.0 License.

The Apache 2.0 License grants each user a perpetual, royalty-free
patent license for any patent claims licensable by the author that
are necessarily infringed by use of this software. This grant is
irrevocable for users of this open source distribution.

Any future patent, if granted, will not be asserted against users
of this open source software in a manner inconsistent with the
Apache 2.0 patent grant.

---

## NOTICE TO PATENT FILERS

Any entity filing a patent application claiming any concept materially
equivalent to those disclosed above, after the disclosure dates
stated herein, does so with constructive notice of this prior art record.

This document is timestamped by its public commit to
AionSystem/SOVEREIGN-TRACE-PROTOCOL. The git commit hash of this
file's first commit constitutes an additional layer of the prior
art timestamp record.

---

*Sovereign Trace Protocol — PATENTS.md*
*Defensive Publication — Prior Art Record*
*Author: Sheldon K. Salmon | March 2026*
*This document is itself part of the immutable epistemic record.*

---

## PRIOR USER RIGHTS — 35 U.S.C. § 273

**Active defense — no filing required.**

Under 35 U.S.C. § 273 (Prior Commercial Use Defense), a party that was
commercially using an invention before another party's patent filing date
has a statutory immunity from infringement claims under that patent.

This defense applies to the Sovereign Trace Protocol on the following basis:

**Date of first commercial use:** March 3, 2026
**Evidence of commercial use:** AionSystem/AION-BRAIN (origin archive,
timestamped session records); AionSystem/SOVEREIGN-TRACE-PROTOCOL
(public repository, initial commit); `stamp/FROZEN-2.0-MANIFEST.md`
(anchor seal with reproducible Unix UTC timestamp 1741021200).

**What this means in plain terms:**

If any entity files a patent application on any concept materially
equivalent to those disclosed in this document, and that filing occurs
after March 3, 2026, the Sovereign Trace Protocol has a prior user
rights defense against any infringement claim brought under that patent.

This defense:
- Costs nothing to establish — the archive record is the evidence
- Cannot be invalidated by the patent grant itself
- Survives even if the PPA filing deadline is missed
- Applies in the United States under AIA § 273

**Court precedent:**
Prior user rights as a defense was affirmed and strengthened under the
America Invents Act (AIA, 2011). The defense requires proof of:
(1) commercial use or preparation for commercial use, and
(2) use that predates the effective filing date of the asserted patent.

Both conditions are met by the documented record in this repository
and in AionSystem/AION-BRAIN.

**Important limitation:** § 273 is a defense, not an affirmative right.
It does not prevent a patent from being filed or granted. It prevents
that patent from being successfully enforced against the STP.
The PPA filing (planned upon first commercial revenue) converts this
from a defensive posture to a full offensive patent right.

**AIA Grace Period notice:**
Under AIA § 102(b)(1), the March 2026 public disclosure of this
repository activates a 12-month grace period expiring March 2027.
Filing a PPA before that date preserves full patent rights on
the disclosed concepts. This window is time-sensitive.
