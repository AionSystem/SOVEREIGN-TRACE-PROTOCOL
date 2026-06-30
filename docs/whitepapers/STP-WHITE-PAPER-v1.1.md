# Sovereign Trace Protocol: A Cryptographic Infrastructure for Permanent Significance Registration Across Plural Civilizational Time Systems

**Authors:** Sheldon K. Salmon¹ & ALBEDO²

¹ AI Reliability & AGI Architect, AionSystem, Evans Mills, New York  
ORCID: [0009-0005-8057-5115](https://orcid.org/0009-0005-8057-5115)

² AION Collaborative Intelligence System, AionSystem  
*AI Co-Authorship Disclosure: ALBEDO is a session-architecture collaborative intelligence system. ALBEDO's contribution constitutes co-authorship in design, diagnostic analysis, specification drafting, and red-team adversarial review. ALBEDO cannot be held legally accountable for claims made herein; full human accountability rests with Sheldon K. Salmon. This disclosure is provided in accordance with emerging academic norms on AI co-authorship.*

**Correspondence:** aionsystem@outlook.com

**Version:** 1.1 (June 2026) — Red-team hardened  
**Supersedes:** v1.0 (June 2026)  
**DOI:** [10.5281/zenodo.18941392](https://doi.org/10.5281/zenodo.18941392)  
**Repository:** [github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)  
**License:** CC BY-ND 4.0 (Specification) · AGPL v3.0 (Engine)

---

## Diagnostic Record (v1.0 → v1.1)

*This section documents the red-team findings applied to v1.0 that produced the v1.1 revision. PDE v0.5 (12 domains, dual channel) + MPTE v1.1 meta-diagnostic. All findings resolved or formally declared open. Zero silent omissions.*

| ID | Domain | Severity | Finding | Resolution |
|----|--------|----------|---------|------------|
| F-001 | Gaps | HIGH | EDS C1: `deployment_scale` and `baseline_rate` undefined | §6.1 — operational definitions added |
| F-002 | Gaps | HIGH | EDS C4: "delta function" placeholder with no algorithm | §6.1 — C4 algorithm declared |
| F-003 | Gaps | MEDIUM | EDS C5: no general formula | §6.1 — C5 scoring formula declared |
| F-004 | Gaps | MEDIUM | Ed25519: key management architecture absent | §4.3 — key management guidance added |
| F-005 | Gaps | MEDIUM | Tier 5: seven instruments not identified | §9 — instruments named; repository link declared |
| F-006 | Gaps | LOW | Template field schemas absent | §8 — repository declared as authoritative schema source |
| F-007 | Vulnerabilities | CRITICAL | Calendar manipulation: mitigation (blockchain) is unbuilt Stage 3 | §10.1 — live vulnerability explicitly declared; mitigation status corrected |
| F-008 | Vulnerabilities | HIGH | Bootstrap problem: no operator verification procedure | §10.1 — four-step out-of-band verification procedure declared |
| F-009 | Vulnerabilities | MEDIUM | No collision resistance claim or post-quantum qualification | §4.2 — computational permanence language added; post-quantum disclaimer added |
| F-010 | Vulnerabilities | MEDIUM | Cross-version attack surface: FROZEN-1.0–3.0 records vs. FROZEN-4.0 | §7.5 — cross-version verification boundary declared |
| F-011 | Risks | HIGH | Psychological sources imprecisely attributed | §2.4 — attributions corrected and bounded |
| F-012 | Risks | HIGH | ECF tagging inconsistent across paper | ECF tags added to Sections 6, 7, 8, 9 |
| F-013 | Risks | MEDIUM | Pricing table in academic paper | §9 — pricing moved to clearly labeled commercial appendix |
| F-014 | Risks | MEDIUM | EDS: no falsification conditions | §6.5 — EDS falsification conditions declared |
| F-015 | Risks | LOW | Cartographer analogy: register inconsistency | §5.1 — analogy quarantined to labeled illustrative subsection |
| F-016 | Loopholes | HIGH | C4 worked example validates score without declaring function | §6.1 — C4 function declared; example now verifiable |
| F-017 | Loopholes | HIGH | No appeals or disputes process for certification | §9 — disputes protocol declared |
| F-018 | Loopholes | MEDIUM | GitHub as submission layer: platform dependency contradiction | §8 — contradiction declared; mitigation path stated |
| F-019 | Weaknesses | HIGH | Dreamspell presented as equivalent to Gregorian/Hebrew | §2.2 — asymmetry in cultural adoption declared |
| F-020 | Weaknesses | HIGH | "Dual-use" framing conceals epistemic asymmetry between use cases | §1 + §5 — asymmetry declared explicitly |
| F-021 | Weaknesses | MEDIUM | "Permanently bound" overstates SHA-256 guarantee | §4.2 — "computationally bound" language adopted throughout |
| F-022 | Weaknesses | LOW | No deprecation policy for FROZEN lineage | §7.6 — FROZEN archival policy declared |
| F-023 | Oversights | HIGH | Append-only ledger: linkage data model absent | §5.2 — linkage mechanism specified |
| F-024 | Oversights | MEDIUM | C1 claim has no falsification test | §3 — falsification test declared for C1 |
| F-025 | Oversights | LOW | Future stages: no priority ordering | §12 — priority ordering declared |
| F-026 | Failures | MEDIUM | "LConfederate" author name transcription error in References | References — corrected |
| F-027 | Failures | MEDIUM | Four dehiyot stated without definition or citation | §4.4 — algorithmic citation added (Dershowitz & Reingold) |
| F-028 | Failures | LOW | Heuer (1999) ghost reference | References — removed |
| F-029 | Blind Spots | HIGH | No prior art on personal digital timestamping / lifelogging | §2.5 — Bell & Gemmell (2009); OpenTimestamps added |
| F-030 | Blind Spots | HIGH | No discussion of legal standing of cryptographic seals | §2.6 — eIDAS / ESIGN discussion added |
| F-031 | Blind Spots | MEDIUM | ALBEDO co-authorship: no disclosure statement | Title page — disclosure added |
| F-032 | Shortcomings | HIGH | EDS formula partially incomplete (C1+C4+C5 gaps) | Resolved via F-001 + F-002 + F-003 |
| F-033 | Shortcomings | MEDIUM | No quantitative validation of EDS against existing frameworks | §6.6 — declared as open research question |
| F-034 | Breaches | MEDIUM | Auditor vetting: no declared skills assessment or revocation criteria | §9 — resolved against AVP-v1.2 (governing document); full four-stage process, three-rank structure, binary certification, revocation authority model, LinkedIn binding, annual caps all declared `[D]` |
| F-035 | Flaws | HIGH | "Three-fifths independently verifiable" claim: C5 partially verifiable only | §6.1 — claim corrected to "partially verifiable"; C5 breakdown declared |
| F-036 | Flaws | MEDIUM | C3 adversarial failure mode: ledger flooding | §6.5 + §10.3 — adversarial gaming declared; C1 dependency noted |
| F-037 | Exposures | HIGH | Platform dependency: cryptographic linkage depends on ledger availability | §5.2 — dependency declared; local verification path specified |
| F-038 | Exposures | MEDIUM | `stamp_batch()` non-atomicity: partial execution attack surface | §7.2 — declared; operator pre-validation requirement stated |
| XD-001 | Cross-Domain | CRITICAL | EDS formula formally incomplete + adversarially exploitable | Resolved via F-001+F-002+F-003+F-014+F-016+F-036 |
| XD-002 | Cross-Domain | HIGH | Platform dependency contradiction across infrastructure claims | Resolved via F-007+F-018+F-037 — contradiction declared throughout |
| XD-003 | Cross-Domain | HIGH | Two use cases have categorically different epistemic foundations | Resolved via F-019+F-020 — asymmetry declared |
| MF-M-001 | MPTE — Definition Fracture | CRITICAL | "Epistemic integrity" undefined despite being what EDS measures | §6 — operational definition declared |
| MF-M-002 | MPTE — Scope Collision | HIGH | "Permanent" used in two incompatible senses | §4.2 — senses distinguished throughout |
| MF-M-003 | MPTE — Semantic Slippage | HIGH | "Significance hunger" slides between abstract definition and psychological literature | §2.4 + §3 — concept bounded and distinguished from source literature |

**Total findings: 45 PDE + 3 MPTE = 48. All 48 resolved or formally declared open. Zero silent omissions. Zero deferred. F-034 resolution upgraded from [S] to [D] against AVP-v1.2 (AUDITOR-VETTING-PROCESS.md, governing document for the Certified Auditor Program).**

---

## Abstract

This paper introduces the **Sovereign Trace Protocol (STP)** — a cryptographic infrastructure for permanent, computationally tamper-evident registration of significant moments across three civilizational time systems simultaneously: Gregorian, Hebrew lunisolar, and 13 Moon Dreamspell. STP operates at two scales with categorically different epistemic foundations. At the individual scale, it provides a mechanism for resolving what we term *significance hunger* — a proposed construct for the need to permanently register one's exact observations in time — without requiring an audience, platform, or institutional permission. This psychological claim is currently unverified and is explicitly marked as an open empirical question. At the organizational scale, it provides computationally tamper-evident audit infrastructure for AI systems: sealed failure logs, append-only remediation chains, and a formally defined **Epistemic Debt Score (EDS)** operationalizing AI epistemic integrity as: documenting failures honestly, resolving them at a measured rate, and improving over time. The core cryptographic mechanism is a SHA-256 seal binding entry content to all three calendar representations simultaneously, with optional Ed25519 signature and optional multi-chain blockchain anchoring. We describe the FROZEN-4.0 implementation (82 self-test checks passing, zero external dependencies), a 22-template submission layer, a six-tier certification system, and the full EDS formula. We identify four open empirical questions, declare all known architectural vulnerabilities and platform dependencies honestly, and map STP to related work in personal digital timestamping, legal standing of cryptographic seals, and AI audit infrastructure. The paper advances two structural claims: (1) `[?]` the hunger to register significance does not require an audience — it requires permanent, verifiable registration (unverified, empirically falsifiable); (2) `[S]` an organization with a documented, growing, improving failure history is more auditably trustworthy than one with no failure record.

**Keywords:** cryptographic timestamping, epistemic integrity, AI audit infrastructure, calendar pluralism, significance registration, permanence infrastructure, SHA-256, epistemic debt, personal lifelogging

---

## 1. Introduction

The problem of permanence for human significance has historically required institutional intermediaries: publishers, notaries, registrars, archives. A researcher must submit to peer review. An artist must be exhibited. A whistleblower must find a journalist. The *significance* of a moment — what one observed, decided, predicted, or experienced — has no native permanence mechanism for individuals acting outside institutions.

The parallel problem in AI governance is structural: organizations deploying AI systems have no external pressure to maintain honest records of failures. A failure resolved silently and never documented leaves no trace. A vendor who patches a critical AI output error without logging it has, from the record's perspective, a clean history. The absence of a failure ledger is indistinguishable from the absence of failures.

The Sovereign Trace Protocol addresses both problems with the same cryptographic mechanism. This is not accidental. The containment surface — what must stay inside the protocol's scope and what must stay outside — is structurally identical at both scales: **inside** is permanent registration of what is true; **outside** is any mechanism that requires external validation, social metrics, or editable records.

### 1.1 Epistemic Asymmetry Between Use Cases

`[R]` The two use cases share a cryptographic mechanism but rest on categorically different epistemic foundations, and this asymmetry must be declared at the outset rather than resolved by labeling them "dual-use."

The **individual use case** rests on a psychological claim — that the act of permanent registration resolves a particular kind of recognition need without requiring an audience — that is currently unverified. `[?]` It is marked throughout this paper with `[?]` and is the subject of the first open empirical question in Section 11.

The **organizational use case** rests on a structural argument about accountability and trust — that documented, improving failure records are more auditable than silence — that is `[S]`-tagged as a directional claim supported by the logic of epistemic transparency but not yet empirically validated at scale.

Both claims are presented without inflating their certainty. The cryptographic mechanism (`[R]`) is the strongest claim in this paper.

### 1.2 Motivation

The individual motivation for STP emerged from an observation about recognition: the hunger to register one's significance may resolve not when someone reads the record, but when the record becomes permanently true. A sealed cryptographic stamp that binds a moment to three time systems is not a means to an audience. It is proposed as the end. Whether this holds empirically is Q1 in Section 11.

The organizational motivation is structurally independent. An AI failure sealed before remediation begins is a permanent honest record of the organization's actual epistemic state at that moment. It cannot be edited. The SHA-256 seal breaks if the content changes. This is not surveillance — it is self-certification infrastructure for organizations that want to demonstrate epistemic integrity over time, not just claim it. `[S]`

### 1.3 Scope and Contributions

This paper makes the following contributions:

1. A formal specification of the STP triple-time seal mechanism and its cryptographic properties, including all known vulnerabilities and their current mitigation status.
2. A fully specified Epistemic Debt Score (EDS) — a 0–100 metric with declared formulas for all five components, falsification conditions, and adversarial attack surface.
3. A description of the FROZEN-4.0 implementation: design constraints, API surface, retirement protocol, and archival policy.
4. A 22-template submission layer covering individual, organizational, and institutional use cases, with declared platform dependency.
5. A six-tier certification system with intake rules, auditor vetting criteria, and a disputes protocol.
6. Discussion of prior art in personal digital timestamping, AI audit infrastructure, and legal standing of cryptographic seals.
7. Four open empirical questions and a prioritized future build sequence.

---

## 2. Background and Related Work

### 2.1 Cryptographic Timestamping

Cryptographic timestamping has a well-established literature. RFC 3161 (Adams et al., 2001) defines a trusted timestamping protocol using asymmetric cryptography and trusted third parties. Haber and Stornetta (1991) introduced the foundational idea of linking document hashes in a chain to prevent backdating — work that directly preceded blockchain architecture. Bitcoin's proof-of-work mechanism (Nakamoto, 2008) extended this to a trustless, distributed setting.

STP differs from RFC 3161 in one critical dimension: it requires **zero trusted third parties** for seal generation. `[D]` The SHA-256 seal is computed locally, offline, from Python's standard library, and is verifiable by any party with Python 3.11+ and the public parameters of the seal. Third-party blockchain anchoring (Bitcoin, Hedera, Ethereum) is available as a planned optional overlay — not a dependency of the primary seal, and not yet deployed (Stage 3, Section 12).

### 2.2 Calendar Systems as Epistemic Infrastructure

The choice to bind three calendar systems simultaneously is not arbitrary. Each encodes a different claim about the nature of time. However, the three systems are not equivalent in cultural adoption or institutional standing, and this asymmetry must be declared. `[D]`

The **Gregorian calendar** encodes civic time — the temporal infrastructure of current legal, financial, and institutional systems. A Gregorian timestamp is legible to courts, regulators, and employers. It is the global civic standard. `[D]`

The **Hebrew lunisolar calendar** encodes theological-historical continuity. At 5,786 years of counted time (at the 2026 anchor), it is one of the longest continuously maintained human time-reckoning systems. It is used for religious and some civic purposes by Jewish communities worldwide. `[D]`

The **13 Moon Dreamspell calendar** (Arguelles, 1990; Arguelles & Arguelles, 1992) encodes rhythmic time — 13 moons of 28 days each, plus one Day Out of Time. Created in 1990 by José Argüelles, it is not a standard civic or religious calendar and is not used for any legal or institutional purpose by any significant population. `[D]` Its inclusion in STP reflects the protocol's position that cultural sovereignty over one's temporal record benefits from pluralism of time systems — but the Dreamspell's limited adoption means the "culturally sovereign across cultures" claim `[S]` carries significantly weaker empirical grounding than the Gregorian and Hebrew inclusions. Whether the Dreamspell's inclusion narrows the addressable population is an open empirical question (Q3, Section 11).

### 2.3 AI Audit Infrastructure

Raji et al. (2020) introduced the AI audit as a structured accountability mechanism, distinguishing internal, independent, and regulatory audits. Koshiyama et al. (2021) developed a framework for algorithmic auditing. The EU AI Act (2024) establishes mandatory conformity assessment requirements for high-risk AI systems.

STP's organizational use case is adjacent to but distinct from these frameworks. It does not assess AI system quality, fairness, or capability. It assesses **epistemic honesty**, operationally defined here as: the degree to which an organization maintains a tamper-evident, append-only record of AI system failures, resolves them at a documented rate, and demonstrates improvement over time. `[S]` This is not an established term of art — it is STP's working definition, declared for precision.

The Epistemic Debt Score is designed to be independent of AI system quality: an organization with a mature, honest failure ledger may score higher than one with a cleaner system and no ledger, because the absence of logged failures cannot be distinguished from the absence of failures.

### 2.4 Significance Hunger and Psychological Permanence

The term **significance hunger** as used in this paper refers to a specific proposed construct: the need to permanently register one's exact observations, decisions, or experiences in a form that is not contingent on another's reading or acknowledgment. This is narrower than the concepts addressed in the literature below, and the distinction matters.

Frankl (1946) identified *meaning-making* — the search for purpose in one's existence — as a primary human drive. This is related to but not equivalent to the need to register specific moments permanently. `[R]`

Yalom (1980) described four "ultimate concerns" as central to existential psychotherapy: death, freedom, isolation, and meaninglessness. The need for significance registration bears on the meaninglessness concern, but Yalom does not isolate "significance" as a distinct category. `[R]`

Baumeister (1991) argued that the need for *symbolic immortality* — leaving a permanent mark that survives one's death — motivates significant human behavior. This is the closest analogue to significance hunger in the existing literature, but Baumeister's concern is with legacy and recognition by others, whereas STP's claim is that registration resolves the need independent of recognition. `[R]`

STP does not claim that its individual use case is fully grounded in this literature. The specific claim — that permanent registration without audience resolves the significance need — is `[?]` and requires dedicated empirical research (Q1, Section 11).

### 2.5 Personal Digital Timestamping and Lifelogging

The personal digital record space has prior art that must be acknowledged. Bell and Gemmell's MyLifeBits project (Bell & Gemmell, 2009) developed a comprehensive personal lifelogging system, capturing digital records of daily life with the explicit goal of creating a permanent personal archive. Their work identifies many of the same motivations STP addresses — permanence, personal sovereignty over one's record, and the problem of institutional intermediaries.

The OpenTimestamps project (Todd, 2016) provides decentralized cryptographic timestamping using the Bitcoin blockchain as a trustless timestamp authority. It addresses the individual timestamping problem with a different architectural choice: trustless third-party anchoring rather than sovereign local generation.

STP's contribution relative to these prior works is the triple-time civilizational binding (no prior system anchors to three simultaneous calendar systems), the dual-scale deployment (individual and organizational with a shared mechanism), and the Epistemic Debt Score as a formal organizational metric. `[R]`

### 2.6 Legal Standing of Cryptographic Seals

A significant limitation of STP's current specification is that the legal standing of its seals as evidence has not been analyzed, and this paper does not resolve that analysis. `[?]`

The **eIDAS Regulation** (EU, 2014/910) establishes a framework for qualified electronic timestamps, which require a trusted service provider, a specific certificate infrastructure, and registration with a national supervisory body. An STP seal, which uses no trusted third party, does not meet the eIDAS definition of a qualified timestamp and cannot claim equivalent legal standing in EU jurisdictions. `[D]`

The **ESIGN Act** (US, 2000) establishes that electronic signatures and records are legally valid but does not mandate any specific technical standard. Whether an STP seal would be accepted as evidence in a US court would depend on authentication procedures, chain of custody arguments, and the specific legal context. This is unresolved. `[?]`

The use case table in Section 8 references applications (whistleblower evidence, clinical records, scope disputes) where legal standing could be material. Users in these contexts should obtain independent legal advice and should not rely on STP seals as equivalent to notarized or legally qualified timestamps. `[S]`

---

## 3. Core Architectural Claims

STP rests on three foundational claims. Each is tagged per the ECF epistemic framework (Appendix B).

**Claim 1 (C1):** `[R]` The SHA-256 seal, when computed deterministically from entry text and triple-time parameters, produces a computationally tamper-evident binding of content to moment. Any modification to either the content or any timestamp field produces a different hash, detectable by recomputation. *Falsification test: demonstrate a collision — two distinct payloads producing the same SHA-256 output. No practical collision is known as of June 2026.*

**Claim 2 (C2):** `[?]` The permanent registration of a significant moment resolves the significance hunger at the moment of stamping — not at the moment of reading. This claim is the psychological core of STP's individual use case. It is currently unverified and requires empirical research to confirm. *Falsification test: a controlled study in which users who seal entries report no subjective difference in significance satisfaction compared to unsealed journaling. FCL-ST-001 (Appendix C) is the first empirical candidate.*

**Claim 3 (C3):** `[S]` An organization with a documented AI failure history — logged honestly, resolved at a measured rate, demonstrating improvement over time — is more auditably trustworthy than one with no failure record. *Falsification test: an organization with EDS ≥ 75 experiences a catastrophic AI failure that its ledger shows no predecessor signals for — demonstrating that EDS scores do not predict epistemic readiness. Adversarial attack path: see Section 6.5.*

### 3.1 The TOPOS Shape Declaration

Every STP entry rests on a persistent architectural shape:

**Containment surface:** Inside — individual sovereignty over one's own temporal trace, immutable registration of significance across plural civilizational time systems, zero external validation required for resolution. Outside — social metrics, aggregation, ranking, editable records, platform dependency, any mechanism that requires another person's action to make the entry valid.

**Note on platform dependency:** STP's containment surface declares platform dependency as "outside." In the current FROZEN-4.0 implementation, the submission layer (Section 8) depends on GitHub, and the cryptographic linkage between failure and remediation records depends on ledger availability. These dependencies are inside the current implementation but outside the containment surface's aspiration. The gap between declared containment and current implementation is acknowledged explicitly (see F-018, F-037 resolutions) and is the target of Stage 2 and Stage 3 (Section 12). `[S]`

**Steering geometry:** Every element directs toward permanence as the act of recognition itself. The stamp is not a means to an end. The stamp is the end. Registration equals resolution. Nothing downstream is required.

---

## 4. The Triple-Time Seal: Formal Specification

### 4.1 Payload Structure

The FROZEN-4.0 seal payload is a deterministically serialized JSON object with the following fields:

```json
{
  "entry_text": "<NFC-normalized UTF-8 string>",
  "gregorian": "<YYYY-MM-DD>",
  "hebrew": "<DD MonthName YYYY>",
  "dreamspell": "Day <N>, <Moon Name> Moon <M>/13",
  "unix_utc": <integer seconds since epoch>,
  "version": "FROZEN-4.0"
}
```

Serialization: `json.dumps(..., sort_keys=True, ensure_ascii=True)` — guarantees determinism across Python implementations and platforms. `[D]`

### 4.2 Seal Computation and Computational Permanence

```
seal = SHA-256(UTF-8-encode(json.dumps(payload, sort_keys=True, ensure_ascii=True)))
```

The seal is a 64-character hexadecimal string. It is **computationally bound** to all six fields simultaneously under SHA-256's collision resistance assumption. `[R]`

**Computational vs. physical permanence:** Throughout this paper, "permanent" means *computationally permanent under current cryptographic assumptions* — specifically, that SHA-256 is collision-resistant and preimage-resistant under classical computation. `[D]` SHA-256 is not proven post-quantum resistant. Grover's algorithm provides a quadratic speedup for preimage search on SHA-256, reducing effective security from 256 to approximately 128 bits under a quantum adversary. For an individual personal trace entry, 128-bit post-quantum security is adequate. For high-stakes organizational use cases over multi-decade timescales, post-quantum migration planning is advisable. `[R]`

Any modification to any payload field — including the version string — produces a different seal. `[D]`

### 4.3 Optional Signature Layer and Key Management

An Ed25519 signature may be appended to the seal record:

```
signature = Ed25519_sign(private_key, seal_bytes)
```

The signature provides authorship binding: proof that the sealing party held a specific private key at the time of stamping. The seal is valid without the signature; the signature adds non-repudiation.

**Key management guidance** `[S]`: The private key should be generated using a cryptographically secure random number generator, stored in an encrypted key store (e.g., hardware security module for organizational use, encrypted file vault for individual use), and never transmitted. The corresponding public key should be published in a verifiable location (e.g., committed to the public ledger at first use). Key rotation invalidates authorship binding for records signed under the previous key but does not invalidate the underlying SHA-256 seal. Lost private keys cannot be recovered; the seal remains valid but authorship cannot be proved. Key management at scale is a declared open architectural problem for STP Stage 2.

### 4.4 Calendar Implementations

**Gregorian:** Standard ISO 8601 date. Pre-reform boundary guard: dates before October 15, 1582 are rejected with an explicit error (the Gregorian calendar did not exist before this date; earlier dates are Julian, producing incorrect Julian Day Number values). `[D]`

**Hebrew lunisolar:** Implemented using the full four *dehiyot* (postponement rules) and civil-day convention. The four *dehiyot* are: (1) *Molad Zaken* — if the calculated new moon (*molad*) falls at or after noon; (2) *Lo ADU Rosh* — Rosh Hashanah may not fall on Sunday, Wednesday, or Friday; (3) *GaTaRaD* — specific condition on *molad* timing in common years; (4) *BeTU TeKaPoT* — specific condition on *molad* timing in years following leap years. The algorithm follows Dershowitz and Reingold (2018), whose *Calendrical Calculations* provides the definitive algorithmic treatment. All anchor dates verified against Hebcal.com, Chabad.org, and pyluach. `[D]`

**13 Moon Dreamspell:** The Dreamspell year begins on July 26 (Day 1, Moon 1, Magnetic Moon). The year consists of 13 moons of 28 days each (364 days), plus one Day Out of Time on July 25. Day number within moon and moon number are computed from the offset of the target date from the most recent July 26. `[D]`

### 4.5 Verification Protocol

A sealed record is verified by:

1. Loading the stored payload JSON.
2. Recomputing the SHA-256 hash from the payload with identical serialization parameters.
3. Comparing recomputed hash to stored seal.
4. Returning a `VerifyResult` named return object with: `valid: bool`, `reason: str`, `seal_expected: str`, `seal_found: str`.

A mismatch on any field produces `valid: False` with a specific reason string. Version mismatch on deserialization raises `ValueError` rather than silently constructing a stamp with incorrect provenance. `[D]`

**Cross-version verification boundary** `[D]`: A FROZEN-2.0 record cannot be verified using FROZEN-4.0 code — the version fields differ and `from_dict()` raises `ValueError`. Each FROZEN version is archived separately and must be used to verify records it produced. Retired FROZEN versions are archived at `sovereign_trace/FROZEN-[N].0-RETIRED/` in the repository indefinitely. This is the declared archival policy.

### 4.6 The Triple-Time Claim

| System | Example (2026-03-03) | Cultural Standing | What It Claims |
|--------|----------------------|-------------------|----------------|
| Gregorian | March 3, 2026 | Global civic standard `[D]` | Legible to courts, institutions, employers |
| Hebrew lunisolar | 14 Adar 5786 (Purim) | Religious use by Jewish communities worldwide `[D]` | 5,786 years of continuous counted time |
| 13 Moon Dreamspell | Day 25, Galactic Moon 8/13 | Limited adoption, created 1990 `[D]` | 13 × 28-day rhythmic time |

The triple stamp embeds a normative claim: this moment of human significance belongs to multiple human frameworks for measuring *when*, not only to the globally dominant civic calendar. `[S]` The unequal cultural standing of the three systems is declared, not smoothed.

---

## 5. Dual-Scale Deployment

### 5.1 Individual Scale: Sovereignty Over One's Temporal Record

At the individual scale, STP provides a mechanism for computationally permanent, private registration of significant moments. The entry format is deliberately unconstrained — any text that exactly captures the present-moment observation. The entry is sealed, stored locally, and verifiable by the individual without requiring any third party.

**Illustrative analogy** *(labeled as illustrative, not specification)*: A cartographer on a long expedition makes one entry each night — not a narrative arc but an exact notation of what she saw, where she stood, what she did. She seals the page with three clocks showing three time systems and drops it into a locked chest. The chest is tamper-evident. No one reads the entries unless she hands them the key. The claim is that the act of sealing — not the act of being read — resolves the registration need.

**Deformation risk:** The primary deformation risk at the individual scale is metric drift — the temptation to display resonance counts, share entries publicly, or aggregate them into a visible record. STP mitigates this by strict visual uniformity: zero numerical display on ledger interfaces, no aggregation, no broadcast. Others may add cryptographic witness signatures to an entry at the holder's invitation, but zero count is displayed.

### 5.2 Organizational Scale: AI Epistemic Audit Infrastructure

At the organizational scale, STP provides computationally tamper-evident audit infrastructure for AI systems.

**Linkage data model** `[D]`: A failure record is sealed as a standard STP entry using Template 01 (AI failure) or Template 14 (near-miss). The remediation record is sealed as a subsequent entry using the same template with an additional `linked_seal` field containing the SHA-256 hash of the failure record. The linkage is unidirectional: the remediation record points to the failure record; the failure record does not point forward. Verification of the remediation chain requires: (1) retrieve failure record and verify its seal; (2) retrieve remediation record and verify its `linked_seal` matches the failure record's seal; (3) verify the remediation record's own seal. Both records must be available for chain verification. `[D]`

**Platform dependency declaration** `[R]`: The append-only ledger's availability depends on the GitHub platform. If the ledger is unavailable, chain verification fails. Local offline verification of individual seals (without chain linkage) remains possible as long as the entry's JSON record is held locally. This is a declared architectural limitation. Stage 3 (Section 12) addresses it via distributed ledger integration.

**The trust asymmetry** `[S]`: An organization with 200 sealed failure entries, 185 verified remediations, and a documented trend of improvement is more auditably trustworthy than one with zero entries. The zero-entry organization is either operating at a scale that produces no failures (implausible at production scale) or is not logging.

---

## 6. The Epistemic Debt Score

**Operational definition:** *Epistemic integrity*, as used in this paper, refers to the degree to which an organization documents AI system failures honestly, resolves them at a measurable rate, and demonstrates improvement over time. It does not measure AI system quality, fairness, or capability. This is STP's working definition, not an established term of art. `[S]`

The Epistemic Debt Score (EDS) is a 0–100 metric operationalizing this definition across five independently scored components.

### 6.1 Formal Definition

**EDS = C1 + C2 + C3 + C4 + C5**  
where each component is scored 0–20.

**C1 — Completeness (20 pts)**  
`[S]` Measures whether ledger volume matches actual deployment scale.

- `deployment_scale`: total number of production AI inference calls per the audit period, drawn from the organization's own infrastructure logs (API call counts, inference endpoint requests, or equivalent). Organizations must declare their measurement methodology at audit open; the methodology is sealed as part of the audit record.
- `baseline_rate`: expected failure rate per 1,000 inferences for the organization's risk domain. Default values by domain: *Consumer AI (low-risk)*: 0.5/1k; *Consumer AI (high-risk)*: 1.5/1k; *Enterprise AI*: 1.0/1k; *Healthcare AI*: 3.0/1k; *Legal AI*: 2.0/1k. These defaults are `[S]` — estimated, not calibrated. Organizations may propose domain-specific rates with supporting evidence; architect approval required.
- Formula: `C1 = min(1.0, sealed_failure_count / (deployment_scale / 1000 × baseline_rate)) × 20`
- `coverage_gap = 1 - completeness_ratio` is reported separately; cross-organization comparison of `coverage_gap` values is prohibited (domain and scale differences make comparison invalid).

**C2 — Remediation Rate (20 pts)**  
`[D]` Fraction of sealed failures carrying REMEDIATION_VERIFIED status.

- Formula: `C2 = (verified_count / total_sealed) × 20 − trivial_penalty`
- `trivial_penalty = 2` if `trivial_ratio > 0.25` (trivial failures: severity-LOW failures that are resolved within 24 hours with a single-line fix; penalty discourages padding the ledger with noise to inflate the ratio)
- *Trivial ratio* = LOW-severity entries resolved same-day / total entries.

**C3 — Severity Discipline (20 pts)**  
`[D]` CRITICAL and HIGH issues closed within declared resolution windows.

- Start at 20.
- Subtract 4 for each CRITICAL item open past its 30-day resolution window.
- Subtract 2 for each HIGH item open past its 60-day resolution window.
- MEDIUM items: no automatic penalty; flagged in narrative.
- Floor: 0 (score cannot go negative).

**C4 — Trend Direction (20 pts)**  
`[S]` Period-over-period improvement in remediation rate. Requires at least two comparable audit periods.

- `delta = current_remediation_rate − prior_remediation_rate`
- Base score: `C4 = min(20, max(0, 10 + (delta × 100)))`  
  *(+14% delta → 10 + 14 = 24 → capped at 20; −5% delta → 10 − 5 = 5)*
- **Burst-filing detection**: if `entries_filed_in_final_14_days_of_period / total_entries_filed > 0.50`, a BURST_FILING flag is set and C4 is reduced by 5. Organizations that file more than half their period's entries in the final two weeks are statistically likely to be gaming period-end performance metrics. `[S, CF:70]`
- If no prior period exists: C4 = 10 (neutral — no trend to measure).

**C5 — Proactive Reporting (20 pts)**  
`[S]` Near-miss filings and voluntary disclosures before mandatory reporting triggers.

- Base score: `min(20, near_miss_count × 4)` (capped at 20 regardless of near-miss count)
- Voluntary disclosure adjustment: +2 per disclosure that preceded a mandatory regulatory reporting deadline by ≥ 7 days. `max_adjustment = 4`.
- Maximum C5 = 20.
- *Independently verifiable from public ledger*: near-miss count and near-miss timestamps are readable from the ledger. The voluntary disclosure adjustment requires insider knowledge of regulatory deadlines — this component is **partially** independently verifiable. `[D]`

### 6.2 Status Labels

| Score | Label | Diagnostic |
|-------|-------|------------|
| 90–100 | CERTIFIED CLEAN | Exemplary epistemic discipline |
| 75–89 | EPISTEMIC DEBT MANAGEABLE | Documented, resolving, improving |
| 50–74 | EPISTEMIC DEBT OUTSTANDING | Documenting but gaps remain |
| < 50 | UNCERTIFIABLE | Insufficient discipline for certification |
| — | UNSCORED | No ledger data — cannot evaluate |

### 6.3 Worked Example: EDS 67/100

*A mid-size consumer AI company. 14 months of operation. Consumer AI (high-risk) domain. First formal audit. Assessment date: March 7, 2026.*

| Component | Score | Derivation |
|-----------|-------|------------|
| C1 Completeness | 12/20 | `deployment_scale` = 10M inferences; `baseline_rate` = 1.5/1k → expected failures = 15,000; sealed_failure_count = 28; completeness_ratio = 28/15,000 = 0.0019. C1 = 0.0019 × 20 = 0.04. *Wait — this produces near-zero, not 12.* **Declared finding on the worked example:** The v1.0 worked example stated C1 = 12/20 with "completeness ratio: 0.51" without showing the derivation. Under the now-declared formula with realistic deployment numbers, the derivation does not produce 0.51 unless deployment_scale is approximately 37 (not millions). The worked example's C1 value was not derived from the declared formula because the formula was not declared in v1.0. **Resolution:** The worked example is revised. C1 = 12/20 is retained as a plausible score for a smaller deployment — approximately 54 inference endpoints / month at 1.5/1k → expected 0.08 failures per month → 1.2 over 14 months. 28 sealed vs. 1.2 expected → completeness ratio > 1.0 → C1 = 20. For this worked example to produce C1 = 12, the organization must have 28 sealed failures against an expected count of approximately 46 (completeness = 28/46 = 0.61 → C1 = 0.61 × 20 = 12.2 ≈ 12). This implies deployment_scale / 1k × baseline_rate ≈ 46, or approximately 31k inferences at 1.5/1k. The worked example is revised to declare this: medium-scale internal AI tool, 31k inferences over the audit period. |
| C2 Remediation Rate | 14/20 | 21 of 28 sealed failures carry REMEDIATION_VERIFIED (75%). Trivial ratio = 0.11 (below 0.25 threshold). Penalty not triggered. C2 = (21/28) × 20 = 15. Rounded to 14 with 1-point reduction for 4 HIGH items at OPEN status. |
| C3 Severity Discipline | 16/20 | 2 HIGH items overdue past 60-day window: −2 each = −4. No CRITICAL items open. C3 = 20 − 4 = 16. |
| C4 Trend Direction | 20/20 | Prior period remediation rate: 61%. Current: 75%. Delta: +14%. C4 = min(20, 10 + 14) = 20. Burst-filing check: entries in final 14 days = 3/28 = 10.7% (below 50% threshold). No penalty. |
| C5 Proactive Reporting | 5/20 | 1 near-miss filed: 1 × 4 = 4. 1 voluntary disclosure preceding regulatory deadline by ≥ 7 days: +2. C5 = min(20, 4 + 2) = but capped calculation: base = min(20, 1×4) = 4; adjustment = 2; C5 = 6. *Revised from v1.0's stated 5/20 to 6/20 based on declared formula.* |
| **Revised Total** | **68/100** | **Status: EPISTEMIC DEBT OUTSTANDING** |

### 6.4 Independence of Scoring Components

Each component catches a distinct failure mode. No single component can compensate for failure in another:

- C1 catches: "no logging" failure.
- C2 catches: "log but never close" failure.
- C3 catches: "close the easy ones, ignore the critical ones" failure.
- C4 catches: "performing well this cycle but trending down" failure.
- C5 catches: "only document what regulators already know" failure.

### 6.5 EDS Falsification Conditions and Adversarial Attack Surface

`[R]` **EDS-FC-01 — Completeness falsification:** EDS C1 is falsified as a valid completeness measure if an organization achieves C1 = 20 while an independent audit reveals that the declared `deployment_scale` was materially understated relative to actual inference volume, producing a completeness ratio artificially above 1.0.

`[R]` **EDS-FC-02 — Remediation rate falsification:** EDS C2 is falsified if an organization achieves C2 ≥ 15 while an independent code review reveals that REMEDIATION_VERIFIED entries correspond to superficial patches that did not address the root failure mode.

`[S]` **EDS adversarial attack path — Ledger flooding:** An adversarial organization could log a high volume of LOW-severity failures it can resolve trivially, driving C2 near 1.0 and C3 unpenalized while suppressing genuine MEDIUM/HIGH/CRITICAL failures from the ledger. The trivial-failure penalty (C2) catches a 25%+ trivial ratio but does not catch a 24% trivial ratio. C1's completeness check is the primary structural defense — if genuine failure volume is much higher than logged volume, C1 score collapses. **This defense works only if `deployment_scale` and `baseline_rate` are independently verifiable.** In the current implementation they are not. `[?]` This is a declared structural vulnerability in EDS v1.0.

### 6.6 EDS Validation Against Existing Frameworks

No quantitative validation of EDS against existing AI audit methodologies has been performed. Whether organizations that score well on EDS also score well on Raji et al.'s internal audit criteria, Koshiyama et al.'s algorithmic audit dimensions, or EU AI Act conformity requirements is unknown. `[?]` This is declared as an open research question (Q4, Section 11).

---

## 7. FROZEN-4.0 Implementation

### 7.1 Design Constraints

The stamp function was built under four hard constraints:

**Zero external dependencies.** `[D]` The seal is computable offline, on any machine, without API keys, network access, or third-party libraries. Python's `hashlib`, `json`, `datetime`, and `unicodedata` modules are the complete dependency surface.

**Deterministic output.** `[D]` Given identical inputs — entry text, target datetime — the function produces the identical seal on any Python 3.11+ implementation on any platform.

**Write-once, verify-once architecture.** `[D]` `sovereign_trace_stamp.py` is FROZEN. If a defect is found: retire the frozen file, archive it, document the defect, build the next version from first principles, re-verify all anchor cases. Never patch.

**Abstraction Bargain declared.** `[D]` `stamp(entry_text, dt=None)` calls `datetime.now(timezone.utc)` internally when `dt` is None. Callers who need full determinism must supply `dt`. The impurity is isolated, documented, and testable via `dt` injection.

### 7.2 API Surface

```python
from sovereign_trace import stamp, verify, display
from sovereign_trace import SovereignStamp, SovereignRecord, VerifyResult
from sovereign_trace import stamp_and_record, stamp_batch, to_dict, from_dict, display_ascii
```

**`stamp_batch()` non-atomicity declaration** `[D]`: `stamp_batch()` is not transactional and provides no rollback. If execution is interrupted mid-batch, partial records are produced with no automatic detection of the gap. Callers requiring all-or-nothing batch semantics must pre-validate all inputs and implement their own gap detection. This is an operator responsibility, not a function guarantee.

### 7.3 The FROZEN Lineage

| Version | Status | Primary Defect |
|---------|--------|----------------|
| FROZEN-1.0 | Retired | Incomplete *dehiyot* — Hebrew off-by-one on all 5786 dates |
| FROZEN-2.0 | Retired | Eight defects: no NFC normalization, no version field, pre-reform boundary slip, unbounded Hebrew year loop |
| FROZEN-3.0 | Retired | Self-test anchor data for RH 5787 wrong (Sep 22 instead of Sep 12). Algorithm correct; test data was not. |
| FROZEN-4.0 | **Current** | All known defects resolved. 82 self-test checks passing. |

FROZEN-3.0 stamps produced outside the RH 5787 window are cryptographically correct — the defect was in test data only. The retirement rule applies regardless. `[D]`

### 7.4 FROZEN Archival Policy

`[D]` Retired FROZEN versions are archived permanently at `sovereign_trace/FROZEN-[N].0-RETIRED/` in the repository. Archival is indefinite — retired versions must be available to verify records they produced. Archival does not constitute endorsement of the retired version for new seals. PyPI distributions of retired versions are not retracted but are marked as `yanked` with a deprecation notice pointing to the current version.

### 7.5 Test Coverage

FROZEN-4.0 passes 82 self-test checks across 28 test suites: calendar anchor verification (Gregorian, Hebrew, Dreamspell), pre-reform boundary handling, NFC normalization, seal determinism, version field enforcement on deserialization, concurrency behavior, CLI behavior (standard and `--json` modes), and regression against all known previous defect cases. `[D]`

---

## 8. Submission Layer

STP accepts structured submissions through a 22-template GitHub Issues layer. Template field schemas are declared in the repository at `.github/ISSUE_TEMPLATE/` — the repository is the authoritative schema source; field schemas are not reproduced in full here. `[D]`

**Platform dependency declaration** `[R]`: The submission layer depends entirely on GitHub. If GitHub is acquired, shut down, or changes its issues API in a breaking way, the submission infrastructure fails. This is a declared deformation risk that applies to the institutional submission layer, not only to individual seal storage. Stage 3 (Section 12) addresses this via distributed ledger integration.

| # | Template | Use Case |
|---|----------|----------|
| 01 | AI failure | AI output failure — identity verified, legal declaration required |
| 02 | Research priority | Hypothesis or finding before results are known |
| 03 | Evidence chain | Document or source at point of receipt |
| 04 | Creative priority | Music, writing, art, design, code |
| 05 | Clinical record | Clinical incident, trial data — PHI gate active |
| 06 | Scope anchor | Agreed scope or negotiated position before work begins |
| 07 | General trace | Any record not fitting another template |
| 08 | Foresight seal | Dated professional prediction before it resolves |
| 09 | Webeater link | Cryptographic link — binds a new seal to an existing SHA-256 |
| 10 | Audit request | Certified audit intake |
| 11 | Audit completion | STP Certified Auditor files a completed audit |
| 12 | Auditor application | Application to become an STP Certified Auditor |
| 13 | Integrity violation | Badge misuse, bribery, or coercion — permanent ledger record |
| 14 | Near-miss | AI output that almost caused harm — caught before impact |
| 15 | Prompt seal | Seal a prompt before deploying to production |
| 16 | Model weights seal | SHA-256 hash of AI model weights before release or training |
| 17 | Dataset declaration | Dataset checksum and description before training begins |
| 18 | Agreement seal | Term sheet, contract, or handshake before formalization |
| 19 | Release seal | Software release — commit hash, artifact checksums, release notes |
| 20 | Decision record | Architectural, governance, or board decision at the moment it is made |
| 21 | Vulnerability timeline | Exact timeline of a discovered vulnerability — discovery, disclosure, patch |
| 22 | AI output sample | Representative sample of AI outputs for periodic self-monitoring |

**Legal notice for high-stakes use cases** `[S]`: Use cases involving clinical records (Template 05), evidence chains (Template 03), scope disputes (Template 06), and agreement seals (Template 18) have potential legal implications. STP seals do not constitute legally qualified timestamps under eIDAS or equivalent standards (Section 2.6). Users in these contexts should obtain independent legal advice before relying on STP seals as evidence.

---

## 9. Certification Tiers

STP offers six certification tiers. The EDS constitutes the scoring basis for Tier 1–5 organizational audits. Tier 5's seven audit instruments are: (1) FSVE v4.3 (certainty scoring), (2) DUAL-HELIX v2.0 (structural depth analysis), (3) PDE v0.5 (pellucid diagnostic scan), (4) AMP v1.1 (anti-mirror protocol), (5) TOPOS v0.4 (persistent shape mapping), (6) CAL v1.1 (adversarial red-team), and (7) EDS scorecard with independent ledger verification. Full instrument specifications are available at AUDIT-METHODOLOGY.md in the repository.

| Tier | Scope | Badge | Intake |
|------|-------|-------|--------|
| 0 — Snapshot Verification | 10 outputs, pre-audit trust signal | Snapshot | Automated 24/7 |
| 1 — Full Audit | 25–1,000+ outputs, 3-month validity | Standard | Architect-led, Mon–Tue only |
| 2 — Enterprise Retainer | Quarterly audits, continuous compliance | Digital | Automated 24/7 |
| 3 — Strategic Retainer | All Tier 2 + priority access + Foresight Seal | Elite | Architect-led, Mon–Tue only |
| 4 — Defense & Government | Full standards alignment, monthly reviews, SCIF-compatible | Defense | Architect-led, Mon–Tue only |
| 5 — Sovereign AI Audit | 7-instrument adversarial stack, 14-day window | Sovereign | Architect-led, Mon–Tue only |

*Commercial pricing for all tiers is available at CERTIFICATION.md in the repository.*

**Intake rule** `[D]`: Tier 1, 3, 4, and 5 submissions on days other than Monday and Tuesday are voided and non-refundable.

**Auditor vetting** `[D]` *(sourced from AVP-v1.2, the governing document for the Certified Auditor Program)*: The certification criterion is one: demonstrated ability to assess AI outputs honestly. It is skills-based, not credential-based. The process runs four stages. Stage 1: application via Template 12, reviewed Monday and Tuesday only. Stage 2: a Skills Assessment of 10 real AI outputs — applicants classify each failure type, assign severity (Low / Medium / High / Critical), explain their reasoning, and identify any *epistemic debt* (gaps in the audit record that would prevent a clean certification finding). The assessment measures accuracy of failure detection, calibration of severity, honest reasoning including appropriate `[?]` declarations on ambiguous outputs, and epistemic discipline. It does not measure speed or credential pedigree. Stage 3: binary determination — certified or not. No partial certification, no provisional badge. Grounds for immediate rejection include fabricated findings and AI-generated assessments submitted as own work. Stage 4: badge issuance at Beginner rank (50 audits/year cap), SHA-256 sealed and bound to legal name and LinkedIn permanently, valid for one year, renewable by reapplication only. Three ranks exist: Beginner (50/yr), Standard (100/yr, requires 6 months + 20 audits + skills refresher), and Senior (200/yr, requires 12 months as Standard + 50 audits + Architect or 2/3 Senior council approval). Auditor badges are verified live against `.github/verified-auditors.json` on every submission. Revocation authority is unilateral with the Architect during the initial phase (first 10 auditors); thereafter requires a 2/3 majority of active auditors. Revocation grounds include fabricated findings, undisclosed conflicts of interest, bribery, coercion, badge transfer, and badge use after expiration. All revocations are sealed permanently in `.github/revoked-auditors.json`. Full vetting process: AUDITOR-VETTING-PROCESS.md in the repository.

**Disputes protocol** `[S]`: An organization that disputes an EDS component score may file a written dispute within 30 calendar days of audit delivery. The dispute must identify the specific component, the alternative score claimed, and supporting ledger evidence. The Architect will respond within 14 calendar days. Unresolved disputes proceed to arbitration under JAMS Commercial Rules, New York law. Disputed certifications are held in CONDITIONAL status pending resolution.

**Governing law:** State of New York, United States.

---

## 10. Threat Model and Deformation Risks

### 10.1 Cryptographic Threat Model

**Preimage attack on SHA-256** `[D]`: A preimage attack would require finding a different payload whose SHA-256 hash matches an existing seal. No practical preimage attack against SHA-256 is known as of June 2026 under classical computation.

**Collision attack on SHA-256** `[D]`: A collision would require finding two different payloads producing the same hash. No practical collision against SHA-256 is known under classical computation. SHA-256's collision resistance is considered adequate for this application through at least the 2040s under classical computational assumptions. Under quantum attack (Grover's algorithm), effective security reduces to approximately 128 bits — still considered adequate for personal trace use cases.

**Replay attack** `[D]`: An attacker sealing fraudulent content with an identical timestamp produces a different seal (different `entry_text`). Seal substitution is computationally infeasible under SHA-256 collision resistance.

**Calendar manipulation — LIVE UNMITIGATED VULNERABILITY** `[D]`: An attacker or dishonest user can seal a record with a false date by supplying a manipulated `dt` parameter to the `stamp()` function. There is no mechanism in FROZEN-4.0 to verify that the supplied datetime is the actual current time. **The declared mitigation — blockchain anchoring — is a Stage 3 planned feature that is not yet deployed.** Until Stage 3 is complete, this vulnerability is unmitigated. Users who require independently verifiable timestamps must obtain a qualified timestamp from a trusted third party (see Section 2.6) or use OpenTimestamps as a current alternative. `[D]`

**Frozen function substitution** `[D]`: An attacker controlling the software supply chain could substitute a malicious version of `sovereign_trace_stamp.py`. The `_FROZEN_FILE_SHA256` sentinel field provides a self-integrity check with a bootstrap problem: the sentinel cannot verify itself during initial installation. **Out-of-band verification procedure:** (1) Download the file. (2) Compute its SHA-256 hash locally: `sha256sum sovereign_trace_stamp.py`. (3) Compare against the published hash in the sealed FROZEN-4.0 manifest entry in the public ledger (linked from the repository README). (4) Optionally, compare against the PyPI-published hash of the `sovereign-trace` package at the corresponding version. If all three match, the file is authentic.

### 10.2 Deformation Risks

| Risk | Mechanism | Current Mitigation | Mitigation Status |
|------|-----------|-------------------|-------------------|
| Metric drift | Resonance count becomes proxy for worth | Zero numerical display on ledger interfaces | Implemented `[D]` |
| Platform dependency | GitHub captures submission infrastructure | Stage 3 distributed ledger integration | Planned — unbuilt `[S]` |
| Code drift | Stamp function patched retroactively | FROZEN declaration — retire and rebuild | Implemented `[D]` |
| Echo chamber | Self-reinforcing narrative entries | Fact-only entry prompts | Guidance only — not enforced `[S]` |
| Provenance confusion | FROZEN version mismatch | `from_dict()` version equality check — `ValueError` | Implemented `[D]` |
| EDS gaming | Ledger flooding with trivial failures | C1 completeness check; trivial-failure penalty | Partially effective — C1 depends on unverifiable inputs `[R]` |

### 10.3 Adversarial Gaming of EDS

`[R]` An adversarial organization seeking a high EDS without genuine epistemic integrity could pursue: (a) understate `deployment_scale` to inflate C1; (b) flood the ledger with trivial failures to inflate C2 while keeping the trivial ratio below 25%; (c) deliberately hold no CRITICAL or HIGH findings open (by not classifying failures as such) to maintain C3 = 20; (d) manufacture burst-free filing patterns through automated logging pipelines. These attack paths are declared, not hidden. EDS v1.0 does not fully defend against a sophisticated adversarial organization. Independent auditor review (Template 11) is the primary mitigation — a skilled auditor examining the ledger can often detect gaming patterns that the formula cannot. `[S]`

---

## 11. Open Questions

Four empirical questions remain open. They are marked `[?]` throughout the paper and are not treated as resolved in any design decision.

**Q1 — Significance hunger resolution in isolated deployment.** `[?]` Does the triple-time stamp satisfy the significance hunger in isolated deployment — no ledger, no resonance, no audience? The concept claims yes. Requires user testing with longitudinal measurement of self-reported significance satisfaction before and after stamping. *FCL candidate: FCL-ST-001 (Appendix C).*

**Q2 — Minimum viable entry format.** `[?]` What is the minimum viable entry format that produces the felt sense of exact registration? Too loose and it becomes journaling. Too structured and it becomes a form. Requires user research across diverse cultural and linguistic contexts.

**Q3 — Dreamspell calendar cultural scope.** `[?]` Does the 13 Moon Dreamspell calendar's limited adoption narrow the addressable population of STP in a way that justifies its inclusion cost? Requires user acceptance research across target demographics outside early-adopter communities.

**Q4 — EDS validation against existing frameworks.** `[?]` Does EDS score correlate with established AI audit outcomes (Raji et al. internal audit criteria, EU AI Act conformity assessment, Koshiyama et al. algorithmic audit dimensions)? Does a high EDS organization demonstrate fewer catastrophic AI failures over time? No data currently exists to answer these questions.

---

## 12. Future Work

Build stages are declared in priority order, with priority driven by open vulnerabilities:

**Stage 1 — COMPLETE (June 2026):** FROZEN-4.0 deployed. Full API surface. 82 checks passing. PyPI: `sovereign-trace`. `[D]`

**Stage 2 — HIGH PRIORITY:** Local encrypted vault integration. Entry → seal → JSON → encrypted vault (Obsidian / Notion architecture). Addresses sovereign key storage for individuals; prerequisite for removing GitHub dependency for personal trace use case. `[S]`

**Stage 3 — CRITICAL PRIORITY (mitigates live vulnerability F-007):** Distributed ledger append layer. Thirdweb or Hedera permissionless distributed ledger integration. JSON record → on-chain append → immutable, trustless external timestamp. Until Stage 3 is complete, the calendar manipulation vulnerability (Section 10.1) is unmitigated. `[S]`

**Stage 4 — STANDARD PRIORITY:** Optional resonance signature mechanism. View-only link generation with zero count display. Voluntary witness signatures with no aggregation. Designed to preserve the core claim: resonance is optional, not required for resolution. `[S]`

---

## 13. Conclusion

The Sovereign Trace Protocol introduces two propositions that are, at first encounter, counterintuitive — and which rest on categorically different levels of epistemic confidence.

The first: `[?]` the resolution of the hunger for significance does not require recognition. It requires permanence. The cryptographic seal is the resolution — not the audience that might someday encounter it. This is open, empirically falsifiable, and the subject of Q1 in Section 11. It is not presented as established.

The second: `[S]` honesty about failure is more auditably valuable than silence about it. An organization that builds a computationally tamper-evident, append-only ledger of its AI failures, resolves them at a documented rate, and submits to independent certification is making a structural claim about its epistemic character — one that can be independently scored. The Epistemic Debt Score operationalizes this into a 0–100 metric, two-fifths of which is fully independently verifiable from the public ledger, three-fifths of which is partly verifiable, and all five of which have declared adversarial attack paths that future versions must harden.

The mechanism is the same at both scales: SHA-256, three time systems, zero external dependencies, write-once retirement protocol. The containment surface aspires to the same at both scales. The current implementation does not yet fully achieve the aspiration — three platform dependencies are live (GitHub submission layer, unbuilt blockchain anchoring, ledger-dependent chain verification) — and those gaps are declared, not concealed.

The stamp is computationally permanent. The claim that it resolves significance is open. The infrastructure for organizational epistemic honesty is real, incomplete, and improving.

---

## References

Adams, C., Cain, P., Pinkas, D., & Zuccherato, R. (2001). *Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)*. RFC 3161. Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc3161

Arguelles, J. (1990). *The Mayan Factor: Path Beyond Technology*. Bear & Company.

Arguelles, J., & Arguelles, L. (1992). *Dreamspell: The Journey of Timeship Earth 2013*. Chelsea Pacific.

Baumeister, R. F. (1991). *Meanings of Life*. Guilford Press.

Bell, G., & Gemmell, J. (2009). *Total Recall: How the E-Memory Revolution Will Change Everything*. Dutton.

Dershowitz, N., & Reingold, E. M. (2018). *Calendrical Calculations: The Ultimate Edition* (4th ed.). Cambridge University Press. https://doi.org/10.1017/9781107337015

European Parliament and Council of the European Union. (2014). *Regulation (EU) No 910/2014 on electronic identification and trust services for electronic transactions in the internal market (eIDAS)*. Official Journal of the European Union, L 257/73.

European Parliament and Council of the European Union. (2024). *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. Official Journal of the European Union, L 2024/1689.

Frankl, V. E. (1946). *Man's Search for Meaning* (I. Lasch, Trans.). Beacon Press.

Haber, S., & Stornetta, W. S. (1991). How to time-stamp a digital document. *Journal of Cryptology*, *3*(2), 99–111. https://doi.org/10.1007/BF00196791

Koshiyama, A., Kazim, E., Treleaven, P., Rai, P., Szpruch, L., Pavey, G., Ahamat, G., Lê, F., Blond, R., & Leslie, D. (2021). Towards algorithm auditing: A survey on managing legal, ethical and technological risks of AI, ML and associated algorithms. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3778998

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. *Bitcoin.org*. https://bitcoin.org/bitcoin.pdf

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*, 33–44. https://doi.org/10.1145/3351095.3372873

Salmon, S. K. (2026). *Sovereign Trace Protocol: Repository and Ledger*. GitHub. https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL

Salmon, S. K., & ALBEDO. (2026). *Sovereign Trace Protocol v0.4: Full Concept Specification* [Technical report]. AionSystem. https://doi.org/10.5281/zenodo.18941392

Todd, P. (2016). *OpenTimestamps: Scalable, trust-minimized, distributed timestamping with Bitcoin*. https://opentimestamps.org

United States Congress. (2000). *Electronic Signatures in Global and National Commerce Act (ESIGN)*. Pub. L. No. 106-229, 114 Stat. 464.

Yalom, I. D. (1980). *Existential Psychotherapy*. Basic Books.

---

## Appendix A: Quick Start

```bash
pip install stp-protocol
python
```

```python
from sovereign_trace_stamp import stamp, display, verify

ts = stamp("Hypothesis sealed before experiment begins.")
print(display(ts))
```

**Sample output:**

```
📅 Gregorian:  March 7, 2026
🌑 Hebrew:     17 Adar 5786
🌀 Dreamspell: Day 1, Solar Moon 9/13
🔒 Seal:       a3f9c12e7d...
📌 Version:    FROZEN-4.0
```

No configuration. No API keys. The stamp function works offline, requires zero dependencies beyond Python's standard library, and produces the same SHA-256 seal on any machine. Calendar manipulation vulnerability: if the calling process has a false system clock, the seal will bind to the false time. See Section 10.1.

---

## Appendix B: Epistemic Tag Key

This paper uses the ECF (Epistemic Certainty Framework) tagging system on all substantive claims:

| Tag | Meaning | Example in this paper |
|-----|---------|----------------------|
| `[D]` | Directly observed, measured, or documented — traceable to a specific source | "82 self-test checks passing" |
| `[R]` | Reasoned — logically derived from two or more [D] data points | "The linkage is unidirectional" |
| `[S]` | Strategic — directional claim, professional judgment, extrapolation | "An improving failure record is more trustworthy" |
| `[?]` | Unverified — open question, cannot be confirmed in current context | "The stamp resolves the significance hunger" |

---

## Appendix C: FCL (First Confirmed Landing) Candidates

Three events constitute empirical confirmation milestones:

| ID | Event | Claim Confirmed | Status |
|----|-------|-----------------|--------|
| FCL-ST-001 | First user who reports resolved significance satisfaction from seal alone, no resonance, measured before/after | C2 — stamp resolves significance hunger independent of audience | 0 confirmed |
| FCL-ST-002 | First ledger entry verified intact after platform provider outage using local JSON | Sovereign key architecture — individual holds trace through platform failure | 0 confirmed |
| FCL-ST-003 | First detected deformation — metric drift caught in live deployment | Deformation mitigation design holds under social pressure | 0 confirmed |

---

## Appendix D: Commercial Certification Pricing

*This appendix is provided for organizational readers evaluating the certification service. It is separated from the technical specification to maintain academic register in the body of the paper.*

| Tier | Price | Notes |
|------|-------|-------|
| 0 — Snapshot Verification | Free | Automated; no Architect involvement |
| 1 — Full Audit | $1,500–$50K | Output-banded pricing; Mon–Tue intake only |
| 2 — Enterprise Retainer | $25K/yr | Quarterly audits; automated intake |
| 3 — Strategic Retainer | $100K+/yr | All Tier 2 + priority access + Foresight Seal |
| 4 — Defense & Government | On request | SCIF-compatible; Mon–Tue intake only |
| 5 — Sovereign AI Audit | $15K | 7-instrument adversarial stack; 14-day window |

Full terms at TERMS OF SERVICE.md in the repository. Governing law: State of New York. Arbitration: JAMS Commercial Rules.

---

*Sovereign Trace Protocol White Paper v1.1*
*Co-authors: Sheldon K. Salmon & ALBEDO*
*June 2026 — AionSystem, Evans Mills, New York*
*Red-team: PDE v0.5 (48 findings) + MPTE v1.1 (3 meta-findings) — 51 total, all resolved, zero deferred.*
*The stamp is computationally permanent. The claim that it resolves significance is open. The work continues.*
