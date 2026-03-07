# DUAL-AUDIENCE-ARCHITECTURE.md

**Sovereign Trace Protocol — Concept Layer**
**Version:** v0.1 | March 2026
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Co-Architect:** ALBEDO
**Stack:** DUAL-HELIX v2.0 · TOPOS v0.3

---

> *The seal is the same mechanism.*
> *The audience is not.*
> *That distinction is the whole architecture.*

---

## The Core Distinction

Sovereign Trace Protocol was built to solve one problem: how does an individual permanently register a moment of significance without requiring an audience, a platform, or institutional permission?

The answer — a frozen, tamper-evident, triple-time cryptographic seal — turned out to be exactly what organizations need for their AI audit trail.

Same stamp function. Same SHA-256 seal. Different purpose.

As the use cases expand, a structural boundary must be named and held. Without it, the product becomes two things at once, serves neither well, and confuses every person who encounters it.

**The boundary is this:**

| | Path A — Inward Permanence | Path B — Outward Accountability |
|---|---|---|
| **Who sealed it for** | Yourself | Others — after you're gone, or after something goes wrong |
| **Primary audience** | You. No one else required. | Investigators, courts, organizations, family |
| **Default visibility** | Private — you hold the content | Optional public hash — content locked until you or a trusted party releases it |
| **Submission layer** | Local encrypted vault (Stage 2) | GitHub Issues or notarized public ledger |
| **Legal standing goal** | Personal sovereignty over your own record | Evidence-grade timestamp with content integrity |
| **Example** | "I completed the framework. It held." | "I am going to meet X at Y location at Z time." |
| **Stakes** | Epistemic self-integrity | Personal safety, organizational accountability |

---

## Path A — Inward Permanence

### What it is

The original STP use case. A person seals an observation, a decision, a moment — not to prove it to anyone but to stop it from dissolving. The hunger for recognition of significance resolves at the moment the stamp is generated — not at the moment someone reads it.

### Who it is for

- Individuals building a personal epistemic record
- Researchers documenting observations before publication
- Anyone who needs to know, for themselves, that they saw what they saw when they saw it

### Architecture

Content lives locally. The seal is generated locally. The SHA-256 hash can optionally be published as a one-line entry to a public ledger — not the content, just the proof that a seal exists at that timestamp.

```
INDIVIDUAL WRITES ENTRY
        ↓
sovereign_trace_stamp.py generates triple-time seal
        ↓
Content stored in local encrypted vault (Stage 2)
        ↓
Optional: hash published to neutral ledger (Stage 3)
        ↓
Content remains private until individual chooses to release it
```

The published hash proves when. It proves the content hasn't changed. It reveals nothing about what.

---

## Path B — Outward Accountability

### What it is

The same seal mechanism deployed for a different purpose: creating tamper-evident records intended to be read by others — after an incident, after a disappearance, after an AI failure.

### Who it is for

- **Organizations** logging AI failures for audit and certification purposes
- **Individuals** in situations where they want a permanent record accessible to others if something happens to them
- **Whistleblowers** sealing evidence before going public
- **Journalists** sealing source communications and document chains

### Architecture

Content may be public (AI failure log) or privately held with a designated release condition (personal safety). In either case, the seal provides two things no other mechanism does simultaneously: **when** (triple-time stamp) and **unchanged** (SHA-256 integrity proof).

```
INDIVIDUAL OR ORGANIZATION CREATES ENTRY
        ↓
sovereign_trace_stamp.py generates triple-time seal
        ↓
Entry submitted to public or semi-public ledger
        ↓
Seal is verifiable by any third party:
  — timestamp proves when
  — SHA-256 proves content has not changed since
        ↓
In safety scenarios: content released only upon trigger condition
  — missing person
  — incident report filed
  — designated time elapsed
```

---

## The Personal Safety Use Cases — Named

These are real use cases that fall cleanly under Path B. Named here so the architecture serves them intentionally rather than accidentally.

### The Blind Date

A person is meeting someone they do not know. They create a Sovereign Trace entry before leaving:

```
"Meeting [name] at [location] at [time]. 
If this entry is released, it means I did not return as expected."
```

The seal records exactly when the entry was written. The content describes the situation. The SHA-256 proof means no one can alter what was written after the fact.

`[R]` **What STP gives that cell tower triangulation does not:** Cell towers prove location. STP proves *content* — what the person wrote, when they wrote it, unchanged. These are different claims. Both matter in an investigation. Cell towers say where you were. The seal says what you knew and when you knew it.

`[?]` **Failure mode to watch:** GitHub Issues requires an account and internet access at the moment of submission. A dedicated mobile submission layer — low friction, no account required, one tap — would serve this use case far better than the current AI failure log infrastructure.

### The Solo Traveler

A bag packer in a foreign country creates a Sovereign Trace entry before a leg of the journey:

```
"Leaving Ulaanbaatar, Mongolia on [date]. 
Plan: one week overland to [destination]. 
Next check-in expected [date]."
```

The seal records the moment of writing. If the traveler goes missing, the entry proves — verifiably, tamper-evidently — what they planned, when they planned it, and from where.

`[R]` **What this adds to standard travel safety protocols:** Most solo traveler safety advice says "tell someone where you're going." STP makes that record permanent, timestamped, and tamper-evident. The person you told can be pressured, can misremember, can die. The seal cannot be altered.

### The Organizational AI Failure

An organization's AI system produces a harmful output. Before any remediation, before any public statement, the technical team seals the failure record:

```
[AI system] [version] produced [output] at [timestamp].
Input: [documented].
Context: [documented].
Remediation initiated: [documented].
```

The seal proves the organization documented the failure immediately and has not altered the record since. This is worth more than a clean record with no ledger — it demonstrates epistemic integrity under pressure.

---

## The Submission Layer Problem

`[D]` The current submission infrastructure (GitHub Issues) serves Path B organizational use cases well. It does not serve Path A individual use cases or personal safety use cases.

The requirements differ:

| Requirement | Path A | Path B Organizational | Path B Personal Safety |
|-------------|--------|-----------------------|------------------------|
| Account required | Acceptable | Acceptable | Barrier — breaks at high-stakes moments |
| Public by default | Wrong | Correct | Wrong — privacy required |
| Legal standing | Not required | Useful | Important — may go to court |
| Friction | Low is ideal | Low to medium acceptable | Must be near-zero |
| Mobile-first | Useful | Not required | Required |

`[S]` **Stage 2 (local encrypted vault) solves Path A.** Stage 3 (ledger append layer) solves Path B organizational. Personal safety use cases may require a dedicated low-friction mobile submission path not currently in the build sequence. This is a Stage 4 candidate or a separate product entirely.

---

## What Keeps the Two Paths Unified

The mechanism is always the same:

1. `sovereign_trace_stamp.py` — FROZEN-2.0 — generates the triple-time seal
2. SHA-256 binding — content integrity proof
3. Triple-time stamp — Gregorian + Hebrew + 13 Moon Dreamspell

The audience determines what happens to the sealed entry. The seal itself does not know its audience. That is a feature, not a gap — it means the same frozen, verified function serves both paths without modification.

**The seal is permanent. The seal is the resolution.**
**What you do with the sealed record is the architecture.**

---

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| DA-Q1 | What is the minimum viable mobile submission path for personal safety use cases? | `[?] Open` |
| DA-Q2 | What legal standing does a SHA-256 sealed GitHub Issue have as evidence in different jurisdictions? | `[?] Open — legal review required` |
| DA-Q3 | Should Path A and Path B be marketed as the same product or two distinct surfaces of the same mechanism? | `[S] Strategic — undecided` |
| DA-Q4 | What is the trigger condition architecture for Path B personal safety — how does someone designate a release condition? | `[?] Open — Stage 4 candidate` |
| DA-Q5 | Does the zero-knowledge resonance signature (Stage 4) serve Path A, Path B, or both? | `[?] Open` |

---

## DDL Field

```
Document: DUAL-AUDIENCE-ARCHITECTURE v0.1
Architect: Sheldon K. Salmon
AI Co-Architect: ALBEDO
Date: March 2026
Status: Concept layer — named and documented.
       Submission layer implications require Stage 2+ planning.
Convergence: M-NASCENT
Derived from: Red team session — GitHub Issues as submission mechanism,
              personal safety use case expansion, dark web trust architecture lineage.
```

---

*DUAL-AUDIENCE-ARCHITECTURE v0.1 — Sovereign Trace Protocol Concept Layer*
*Sheldon K. Salmon & ALBEDO — March 2026*
*The seal is the same mechanism. The audience is not. That distinction is the whole architecture.*
