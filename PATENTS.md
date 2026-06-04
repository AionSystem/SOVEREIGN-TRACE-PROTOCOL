# PATENTS.md — Defensive Publication & Prior Art Record

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & ADI/AGI Architect
**Version:** 1.1 | June 2026
**Date of first disclosure:** March 3, 2026
**Repository:** AionSystem/SOVEREIGN-TRACE-PROTOCOL
**Origin archive:** AionSystem/AION-BRAIN

> **IMPORTANT DISCLAIMER:** This document is for informational purposes only
> and does not constitute legal advice. The author is not a patent attorney.
> Consult qualified patent counsel for any patent filing or infringement analysis.

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

**Prior art records (reproducible – illustrative examples):**

*Historical example (FROZEN-2.0, March 3, 2026):*
Entry: "Origin trace — Sovereign Trace Protocol FROZEN-2.0 sealed at session of birth."
Gregorian: March 3, 2026
Hebrew: 14 Adar 5786
Dreamspell: Day 25, Galactic Moon 8/13
Unix UTC: 1741021200
Seal: 19276f3fbdd02960ffab7eb9ed044e023cb68ffc426179c71cb1476d07d477e2

text

*Current example (FROZEN-4.0, June 4, 2026):*
Entry: "Defensive publication update — Sovereign Trace Protocol FROZEN-4.0."
Gregorian: June 4, 2026
Hebrew: 18 Sivan 5786
Dreamspell: Day 2, Solar Moon 10/13
Unix UTC: 1741372800
Seal: 8f3a9c2e7d1b4f6a9c2e7d1b4f6a9c2e7d1b4f6a9c2e7d1b4f6a9c2e7d1b4f6a

text

> **Note on examples:** The example seals are illustrative. The prior art
> disclosure is the description of the method, not the specific seal output.
> The method is version‑independent; different frozen versions are
> implementations of the same inventive concept.

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
5. The designation carries a version number (e.g., FROZEN-4.0) that
   increments with each new creation from first principles,
6. All outputs produced by a frozen module carry implicit provenance
   tied to that version designation.

**Prior art record:** FROZEN-4.0 designation applied to
`stamp/sovereign_trace_stamp.py` on June 4, 2026 in this repository.
FROZEN-1.0 was retired without a functional release (no defect record
required). FROZEN-2.0 and FROZEN-3.0 are archived in `stamp/FROZEN-X.0-RETIRED/`.

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
**no later than March 2027** (within the 12‑month AIA grace period
from the first public disclosure in March 2026). Filing a PPA within
this window preserves the ability to seek patent rights while
maintaining the open source nature of the code under the Apache 2.0 License.

The Apache 2.0 License grants each user a perpetual, royalty‑free
patent license for any patent claims licensable by the author that
are **necessarily infringed by the use of this software as distributed**.
This grant is irrevocable for users of this open source distribution.
The patent license applies to your use of the Sovereign Trace Protocol
code; it does not extend to your own separate inventions unless they
necessarily infringe on patents that cover this protocol.

Any future patent, if granted, will not be asserted against users
of this open source software in a manner inconsistent with the
Apache 2.0 patent grant.

Failure to file a PPA does not invalidate the defensive publication
or the prior user rights described below.

---

## NOTICE TO PATENT FILERS

Any entity filing a patent application claiming any concept materially
equivalent to those disclosed above, after the disclosure dates
stated herein, does so with **actual notice** (if they have reviewed
this document) of this prior art record. This document does not
provide “constructive notice” in the legal sense (which requires
USPTO publication), but it serves as evidence of prior use and may
be used in opposition or cancellation proceedings.

This document is timestamped by its public commit to
AionSystem/SOVEREIGN-TRACE-PROTOCOL. The git commit hash of this
file's first commit constitutes an additional layer of the prior
art timestamp record.

---

## PRIOR USER RIGHTS — 35 U.S.C. § 273

**Active defense — no filing required.**

Under 35 U.S.C. § 273 (Prior Commercial Use Defense), a party that was
commercially using an invention before another party's patent filing date
has a statutory immunity from infringement claims under that patent.
This defense is not automatically invalidated by the patent grant,
but its applicability may be determined by a court.

This defense applies to the Sovereign Trace Protocol on the following basis:

**Date of first commercial use:** March 3, 2026
**Evidence of commercial use:** AionSystem/AION-BRAIN (origin archive,
timestamped session records); AionSystem/SOVEREIGN-TRACE-PROTOCOL
(public repository, initial commit); `stamp/FROZEN-4.0-MANIFEST.md`
(anchor seal with reproducible Unix UTC timestamp 1741372800).

**What this means in plain terms:**

If any entity files a patent application on any concept materially
equivalent to those disclosed in this document, and that filing occurs
after March 3, 2026, the Sovereign Trace Protocol has a prior user
rights defense against any infringement claim brought under that patent.

This defense:
- Costs nothing to establish — the archive record is the evidence
- Is not automatically invalidated by the patent grant (but must be proved)
- Survives even if the PPA filing deadline is missed
- Applies in the United States under AIA § 273

**Important limitation:** § 273 is a defense, not an affirmative right.
It does not prevent a patent from being filed or granted. It provides
a potential defense against enforcement.

---

## IPFS ANCHOR

To provide an additional layer of distributed, immutable timestamping,
this document will be pinned to IPFS. The CID will be recorded here
once available.

`[S]` IPFS CID: [TO BE RECORDED]

---

*PATENTS.md — v1.1 (June 2026)*
*Sovereign Trace Protocol | Sheldon K. Salmon — AI Reliability & ADI/AGI Architect*
*This document is part of the immutable epistemic record.*
