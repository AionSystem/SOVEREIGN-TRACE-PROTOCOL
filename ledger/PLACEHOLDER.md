# Ledger — Append Layer

**Status:** Not yet built — Stage 3 of build sequence
**Target:** Thirdweb or Hedera permissionless distributed ledger

---

## What This Will Be

Stage 3 of the Sovereign Trace Protocol build sequence.

The stamp function (Stage 1) produces a sealed JSON record. The vault integration
(Stage 2) stores that record locally, encrypted, sovereign. This layer — Stage 3 —
appends that record to a permissionless distributed ledger.

Once appended, the trace is not just locally permanent. It is network-permanent.
It exists on infrastructure that requires no platform, no vendor, no relationship
to remain intact.

---

## Design Parameters (Planned)

**Input:** Sealed JSON record from `sovereign_trace_stamp.py` + entry text

**Operation:** Single append call — no read, no modify, no delete

**Output:** Transaction hash — the network's confirmation that this trace
exists at this moment in the distributed record

**Ledger candidates:**
- **Thirdweb** — EVM-compatible, low-cost append, strong developer tooling
- **Hedera Hashgraph** — low latency, deterministic finality, enterprise-ready

**Sovereignty constraint:** The append layer must not require the individual
to give the ledger provider access to the entry text. Options:
1. Append only the seal (hash) — content stays sovereign, existence is provable
2. Append encrypted payload — content is sovereign, full record is preserved on-chain

**Decision pending:** Option 1 vs Option 2. The seal alone proves existence and integrity
without exposing content. This is consistent with the containment surface: what is on-chain
is the proof, not the trace.

---

## What Stage 3 Does Not Do

- It does not replace the local vault (Stage 2)
- It does not require internet connectivity to generate a stamp
- It does not make the entry text public
- It does not introduce a platform the individual depends on for stamp generation

The ledger is an additional layer of permanence, not a dependency.
Stamps produced before Stage 3 is built are valid and permanent.
The ledger append is a supplement to local permanence, not a prerequisite for it.

---

## Current State

**Stage 1 — COMPLETE:** `stamp/sovereign_trace_stamp.py` — FROZEN-2.0

**Stage 2 — PLANNED:** Local encrypted vault integration

**Stage 3 — PLANNED (this directory):** Ledger append layer

**Stage 4 — PLANNED:** Optional resonance signature mechanism

---

*Sovereign Trace Protocol — Ledger Placeholder*
*Stage 3 of 4 — not yet built*
*This file is the structural anchor for the coming implementation.*
*March 2026*

