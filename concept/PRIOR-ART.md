# PRIOR-ART.md

**Sovereign Trace Protocol — Concept Layer**
**Version:** v1.0 | June 2026
**Author:** Sheldon K. Salmon — AI Reliability & AGI Architect
**Co-Architect:** ALBEDO
**Purpose:** Defensive documentation of what existed before STP v4.0, what STP v4.0 introduces, and when.

---

> *"The mechanism that gives an individual temporal sovereignty over their own record
> also gives an organization cryptographic proof of their epistemic integrity."*

---

## Purpose of This Document

This document exists for two reasons:

**Defensive:** To establish clearly and permanently what prior art existed before Sovereign Trace Protocol, so that no future claim can assert that STP was obvious, derivative, or already existed in equivalent form.

**Constructive:** To position STP accurately in its engineering lineage — acknowledging what it builds on while identifying precisely what it introduces that did not previously exist in this combination and for this purpose.

This document was sealed as part of the STP repository. Its existence at this date is itself a Sovereign Trace entry.

---

## What Existed Before STP

### Cryptographic Timestamping

RFC 3161 (Internet X.509 PKI Time-Stamp Protocol) — established 2001. Provides cryptographic proof that a document existed at a specific time. Requires a trusted third-party timestamp authority (TSA). The trust claim is institutional — you are trusting the TSA to be honest and solvent. Widely used in legal and financial systems.

**What it does not provide:** Triple-time civilizational framing. Zero-dependency self-contained verification. Human-readable output designed for individual use. Institutionally independent verification (RFC 3161 requires the TSA).

### Blockchain Timestamping

Bitcoin OP_RETURN (2014 onwards). Ethereum event logs. Hedera consensus timestamps. All provide append-only, tamper-evident timestamping on distributed ledgers. Trust is mathematical — no single institution controls the record.

**What they do not provide:** Human-readable triple-time civilizational framing. Zero-dependency local generation. A complete submission and ledger protocol for non-technical users. The stamp function itself — these services timestamp hashes you provide, they do not generate the structured sealed record.

### Open Timestamps (opentimestamps.org)

Peter Todd's Open Timestamps project — provides Bitcoin-anchored timestamping, open source, institutionally independent. Closest prior art to STP's trust model.

**What it does not provide:** Triple-time framing. Human-readable output. Submission protocol. Ledger architecture for organizational accountability. The personal sovereignty framing. The structured issue-template submission layer.

### Academic Pre-Registration

OSF (Open Science Framework) pre-registration. AsPredicted.org. ClinicalTrials.gov. All provide timestamped hypothesis registration before results are known.

**What they do not provide:** Cryptographic sealing of the exact content. Institutional independence (all require an account with a specific platform). Use outside academic contexts. Triple-time framing. A mechanism that works for AI failures, creative works, evidence chains, and personal moments simultaneously.

### Warrant Canaries

Pioneered by various privacy-focused organizations post-2013. Provides proof-of-absence timestamping — regular publication of a statement that no government orders have been received, with absence of the statement as the signal.

**What it does not provide:** Content sealing. SHA-256 binding. Triple-time framing. Submission protocol. Not designed for individual or organizational accountability use.

### Legal Notarization

Traditional notary services. Electronic notarization (RON — Remote Online Notarization). DocuSign eNotary. Provides identity-verified timestamped document sealing with legal standing in most jurisdictions.

**What it does not provide:** Institutionally independent verification. Zero-cost operation. Self-contained cryptographic proof. Triple-time civilizational framing. Open source mechanism. Submission at scale for AI failure logging.

### GitHub Issues as Evidence

Journalists and researchers have informally used GitHub Issues and commits as timestamped public records. Not a formal protocol. No cryptographic seal. No structured submission format. No ledger architecture.

### Abuse Detection in Issue Tracking

Generic spam filters and GitHub's own moderation tools exist. No prior system implements a **tiered (green/yellow/red) abuse detector** that scores content for prohibited patterns, decodes encoded attacks, and routes borderline cases to manual review — all while allowing appeal and tracking repeat offenders.

### Single-Blockchain Anchoring

Individual projects have anchored hashes to Bitcoin or Ethereum. No prior open-source system implements **multi‑chain anchoring** (Bitcoin, Hedera, Ethereum, and optionally Stellar) of a Merkle root from batched GitHub issue seals, with automated weekly publication via GitHub Actions.

---

## What STP v4.0 Introduces That Did Not Previously Exist In This Combination

The following combination has not previously existed as a single open-source, zero-dependency, institutionally independent protocol:

**1 — Triple-time civilizational framing as a first-class design element.**
No prior timestamping protocol binds content simultaneously to Gregorian, Hebrew lunisolar, and 13 Moon Dreamspell calendars as a deliberate claim about civilizational significance. This is not redundancy — it is a philosophical and architectural assertion that a moment of significance deserves to be held across every major framework for measuring *when*.

**2 — Zero-dependency self-contained verification.**
FROZEN-4.0 uses only Python stdlib. No network call. No external service. No account. The verification is in the mathematics of the file itself. Anyone with Python can verify any seal independently without trusting STP as an institution. Prior art either requires a TSA (RFC 3161), a blockchain node (Open Timestamps), or a platform account (OSF, AsPredicted).

**3 — Frozen deployment architecture as an integrity guarantee.**
The FROZEN declaration — written once, verified once, deployed permanently, never patched — is a novel architectural commitment. The stamp is only permanent if the code that generates it is also permanent. FROZEN-1.0, FROZEN-2.0, and FROZEN-3.0 were retired and archived when defects were found rather than patched. This retirement-not-patching protocol did not previously exist in timestamping infrastructure.

**4 — Dual-use personal and organizational protocol on a single mechanism.**
Prior art either serves individuals (notary, creative copyright) or organizations (RFC 3161, blockchain anchoring) — rarely both from the same mechanism. STP's design premise — that the mechanism which gives an individual temporal sovereignty over their own record also gives an organization cryptographic proof of epistemic integrity — is architecturally novel.

**5 — Structured submission protocol for AI failure accountability.**
No prior timestamping protocol includes a structured, legal-declaration-bearing submission system specifically designed for AI output failure documentation at organizational scale. STP v4.0 provides **31 issue templates** covering AI failures, research priority, evidence chains, creative works, clinical records, scope anchors, general traces, foresight seals, WEBEATER links, audit requests/completions, auditor applications, integrity violations, near‑misses, prompt seals, model weight seals, dataset declarations, agreement seals, release seals, decision records, vulnerability timelines, AI output samples, bias audits, red team engagements, model cards, human oversight logs, code snippets, research logbooks, identity anchors, temporal commitments, and general feedback.

**6 — Issue-template submission layer with permanent URL + SHA‑256 hash binding for evidence.**
The use of GitHub Issue templates as the submission interface for a cryptographic ledger — with mandatory **permanent URL + SHA‑256 hash** fields instead of unsupported file uploads — is a novel combination of GitHub infrastructure and cryptographic permanence architecture.

**7 — Cryptographic link layer (WEBEATER).**
`REF_SEAL` field binding a new stamp to a previous SHA-256, creating a verifiable chain of significance between two entities without requiring a centralized authority. Specified and deployed.

**8 — Tiered abuse detection (green/yellow/red).**
A GitHub Action workflow that scans every new issue for prohibited content (threats, CSAM, doxing, credential leaks) using pattern matching and optional Perspective API. Scores content from 0 to 1. Green passes automatically; yellow adds a `needs-review` label without closing; red closes, locks, logs, and tracks repeat offenders. Decodes base64 and rot13 to catch encoding tricks. Includes an appeal process via email. No prior open‑source timestamping protocol includes this as part of its submission layer.

**9 — Multi‑chain blockchain anchoring of batched seals.**
A script that periodically computes a Merkle root of all new STP seals (from GitHub issues) and posts that root to **Bitcoin (OP_RETURN), Hedera Consensus Service, Ethereum (contract or raw tx), and optionally Stellar**. Runs weekly via GitHub Actions at no cost (testnets) or minimal cost (mainnet). Provides decentralized, permanent proof of seal batches across multiple independent ledgers — a level of redundancy not seen in any single prior art.

**10 — GitHub Composite Action `stp-seal`.**
A reusable GitHub Action that allows any repository to seal a message or file with STP, outputting SHA‑256 hash and triple‑time stamp, with optional GitHub issue ledger entry. Hardened against command injection, path traversal, and symlink escape. No prior timestamping protocol provides a turnkey GitHub Action for CI/CD pipelines.

---

## Date of Introduction

All elements above were introduced in the Sovereign Trace Protocol by Sheldon K. Salmon, with the following milestones:

| Milestone | Date |
|-----------|------|
| FROZEN-1.0 specified and deployed | February 2026 |
| FROZEN-1.0 defect identified — Hebrew dehiyot incomplete | March 2026 |
| FROZEN-1.0 retired, archived | March 2026 |
| FROZEN-2.0 specified, verified, deployed | March 3, 2026 |
| FROZEN-2.0 retired (eight defects) | March 2026 |
| FROZEN-3.0 deployed, retired (self‑test anchor data) | May 2026 |
| **FROZEN-4.0 deployed** (82 self‑tests, all known defects resolved) | **June 2026** |
| 31 issue templates finalised and hardened | June 4, 2026 |
| Tiered abuse detector and multi‑chain anchor deployed | June 4, 2026 |
| GitHub Composite Action `stp-seal` released | June 4, 2026 |
| This prior art document updated to v1.0 | June 2026 |

---

## What STP Does Not Claim

STP does not claim to have invented: cryptographic hashing, SHA-256, the Hebrew lunisolar calendar algorithm (Dershowitz & Reingold), the 13 Moon Dreamspell calendar (José Argüelles), blockchain timestamping, academic pre-registration, GitHub Issues, generic spam filtering, or public blockchains.

STP claims the specific combination, framing, architecture, and purpose described in this document as original work by Sheldon K. Salmon.

---

## DDL Field
Document: PRIOR-ART v1.0
Architect: Sheldon K. Salmon
AI Co-Architect: ALBEDO
Date: June 2026
Purpose: Defensive IP documentation. Prior art established. STP v4.0 novelty documented.
Status: Sealed at time of repository publication.

text

---

*PRIOR-ART v1.0 — Sovereign Trace Protocol Concept Layer*
*Sheldon K. Salmon & ALBEDO — June 2026*
*The mechanism is new. The mathematics it builds on is not. Both are documented here.*
