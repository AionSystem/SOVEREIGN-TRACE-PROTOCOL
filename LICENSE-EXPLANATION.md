# LICENSE EXPLANATION

**Sovereign Trace Protocol (STP) & AION Constitutional Stack**
**Plain-language guide to the dual-license architecture**
**Author:** Sheldon K. Salmon — AI Reliability & ADI/AGI Architect
**Version:** 2.0 | June 2026
**Supersedes:** v1.1 (Triple License Architecture)

---

## WHY THE ARCHITECTURE CHANGED

Most repositories ship with a single permissive license. That architecture is a wealth-extraction trap for the original author. Under Apache 2.0 or standard GPL v3, a mega-capacity entity can ingest the code, deploy it as a closed-source SaaS, generate billions in regulatory goodwill, and pay the architect zero dollars. 

This repository ships with a split-license perimeter. The specification is immutable. The engine is copyleft. The corporate extraction mechanism is active.

Here is what each component does in plain language, and which one applies to you.

---

## LICENSE 1 — CC BY-ND 4.0 (The Specification)

**File:** `LICENSE_SPEC.md`
**Applies to:** All `.md` documentation files (e.g., the Sovereign Trace Protocol specification, Constitution texts).
**The Mechanism:** Creative Commons Attribution-NoDerivatives 4.0 International.

**What you can do:**
- Read, cite, and share the document.
- Timestamp it via DOI/SSRN to establish prior art.
- Use it as a reference standard for academic or non-commercial research.

**What you cannot do:**
- Create derivative works (you cannot fork the Markdown and publish "STP v2.1" or "Constitution v2.3").
- Use the specification text for commercial purposes without explicit written permission.

**Why this exists:**
The specification is the canonical standard. If it is open-source, corporations will fork it, dilute the canonical hash, and destroy the mutual recognition mechanism. CC BY-ND ensures the standard remains immutable while remaining freely accessible for community adoption and academic citation.

---

## LICENSE 2 — AGPL v3.0 (The Runtime Engine)

**File:** `LICENSE_ENGINE.md`
**Applies to:** All `.py` source code files and executable implementations (e.g., `constitutional_engine_v2.2.py`).
**The Mechanism:** GNU Affero General Public License v3.0.

**The SaaS Poison Pill:**
Standard GPL v3 only triggers when you *distribute* a binary or source file. If a company runs GPL code on a backend server (SaaS), they do not distribute it, and the copyleft fails. 
The AGPL closes this loophole. Section 13 (Remote Network Interaction) mandates that if you use this engine to provide a service over a network, you **must** open-source your entire application stack under the same AGPL license.

**What you can do:**
- Download, modify, and run the engine for personal, academic, or internal open-source projects.
- Build open-source tools that integrate with the engine, provided your entire stack is also AGPL.

**What you cannot do:**
- Run this engine as part of a proprietary, closed-source SaaS product.
- Integrate this engine into a corporate backend without open-sourcing your entire proprietary codebase.

**Why this exists:**
It forces a binary choice on enterprise entities: either contribute your modifications back to the open-source ecosystem (strengthening the standard), or contact the architect to purchase a commercial license.

---

## LICENSE 3 — COMMERCIAL DUAL-LICENSE (The Enterprise Option)

**File:** `LICENSE-COMMERCIAL.md` (Available upon request)
**Applies to:** Organizations that want to integrate the Runtime Engine into a proprietary, closed-source, or commercial product without triggering the AGPL copyleft obligations.

**When you need this:**
- You are building a closed-source SaaS platform that requires the STP/AION engine for compliance.
- You want to embed the engine in a proprietary enterprise product.
- You require the "Sovereign Certified" badge or AION-Registry listing for commercial audit purposes.

**What it gives you:**
- A proprietary license to use the `.py` engine without open-sourcing your stack.
- Legal clarity for enterprise procurement and compliance teams.

**How to get it:**
File a `commercial-license-inquiry` issue in this repository, or email aionsystem@outlook.com. All terms are negotiated in writing.

---

## WHICH LICENSE APPLIES TO YOU?

| Your Situation | Applicable License |
|----------------|--------------------|
| Reading, citing, or sharing the Markdown specification | **CC BY-ND 4.0** — Free |
| Academic research or non-commercial analysis | **CC BY-ND 4.0** — Free |
| Running the Python engine locally for personal/academic use | **AGPL v3.0** — Free |
| Building an open-source project (fully AGPL-compliant stack) | **AGPL v3.0** — Free |
| Running the engine on a server for a proprietary/closed-source SaaS | **Commercial License Required** |
| Integrating the engine into a closed-source enterprise product | **Commercial License Required** |
| Offering certification/compliance services to third parties | **Commercial License Required** |

**If you're not sure:** File an issue with the label `license-question`. You will get a plain-language answer.

---

## THE LITIGATION POISON PILL

If **you** initiate legal proceedings against Sheldon K. Salmon arising from this repository, **your** licenses terminate automatically: your CC BY-ND rights, your AGPL v3 rights, and any commercial license in effect. 

All terminations are automatic. No separate court action is required. This applies only to the party initiating suit. It does **not** affect any other user's license rights.

This is the open-source equivalent of a dead man's switch.

---

## DISCLAIMER

This document is for informational purposes only. It does **not** constitute legal advice. You should consult a qualified attorney for any legal questions regarding license compliance or commercial deployment. 

---

## WHAT YOU DO NOT NEED TO WORRY ABOUT

If you are a researcher, student, or open-source developer reading the spec or running the engine locally to learn from it, you have zero legal exposure. The licenses are designed to protect the architect from corporate extraction, not to restrict academic freedom or community adoption. 

Just read, learn, and build.

---

*LICENSE-EXPLANATION.md — v2.0 (June 2026)*  
*Sovereign Trace Protocol & AION Constitutional Stack | Sheldon K. Salmon — AI Reliability & ADI/AGI Architect*  
*Plain language. Not legal advice. Consult qualified counsel for commercial deployment.*
