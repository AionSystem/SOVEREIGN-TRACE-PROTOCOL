<div align="center">

# SOVEREIGN TRACE PROTOCOL — REPOSITORY STRUCTURE

**Complete file manifest · FROZEN-4.0 · June 2026**

[![Permanent](https://img.shields.io/badge/PERMANENT-FROZEN--4.0-2E7D32?style=flat-square&logo=git&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![PyPI](https://img.shields.io/pypi/v/sovereign-trace?style=flat-square&color=2E7D32&label=PyPI)](https://pypi.org/project/sovereign-trace/)
[![Dependencies](https://img.shields.io/badge/DEPS-stdlib%20only-616161?style=flat-square)](https://docs.python.org/3/library/index.html)
[![Tests](https://img.shields.io/badge/TESTS-30%20suites-1565C0?style=flat-square&logo=pytest&logoColor=white)](./tests/)
[![Ledger](https://img.shields.io/badge/LEDGER-66%20entries-4527A0?style=flat-square&logo=hashnode&logoColor=white)](./ledger/)
[![Templates](https://img.shields.io/badge/TEMPLATES-22%20issue%20types-0288D1?style=flat-square)](./ISSUE_TEMPLATE/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-darkgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: Commercial](https://img.shields.io/badge/License-Commercial-orange.svg)](./LICENSE-COMMERICAL.md)
[![Legal Posture](https://img.shields.io/badge/LEGAL-Posture%20Active-8B0000?style=flat-square)](./LEGAL-POSTURE.md)

</div>

---

```
sovereign-trace-protocol/
│
│  ── ROOT ──────────────────────────────────────────────────────────────────
│
├── README.md
├── STP-logo.svg
├── QUICKSTART.md
├── HOW-TO-SUBMIT.md
├── repo_structure.md
├── pyproject.toml
├── pytest.ini
├── .gitignore
│
│  ── CERTIFICATION & AUDIT ─────────────────────────────────────────────────
│
├── CERTIFICATION.md
├── AUDIT-METHODOLOGY.md
├── AUDITOR-VETTING-PROCESS.md
├── EPISTEMIC-DEBT-SCORE.md
├── STANDARDS-ALIGNMENT.md
├── METHODOLOGY.md
│
│  ── LEGAL ──────────────────────────────────────────────────────────────────
│
├── LICENSE
├── LICENSE-COMMERICAL.md
├── LICENSE-EXPLANATION.md
├── LICENSE-GPLv3.md
├── NOTICE
├── TERMS OF SERVICE.md
├── LEGAL-POSTURE.md
├── PRINCIPLES.md
├── PATENTS.md
├── TRADEMARK.md
├── TRADEMARK-USAGE-POLICY.md
├── CONTRIBUTOR-TERMS.md
├── CONTRIBUTOR-LICENSE-AGREEMENT.md
├── DATA-PROCESSING-AGREEMENT.md
├── MUTUAL-NDA.md
├── UNILATERAL-NDA.md
├── EXPORT-CONTROL.md
├── CITATION.cff
│
│  ── POLICY & ETHICS ─────────────────────────────────────────────────────
│
├── ACCEPTABLE-USE-POLICY.md
├── AI-ETHICS-STATEMENT.md
├── PRIVACY-POLICY.md
├── SECURITY.md
├── SECURITY-INSIGHTS.yml
│
│  ── OPERATIONS ──────────────────────────────────────────────────────────
│
├── DISASTER-RECOVERY.md
├── NON-RECOURSE-STATEMENT.md
│
│
│  ── .GITHUB ─────────────────────────────────────────────────────────────
│
├── .github/
│   ├── FUNDING.yml
│   ├── SECURITY.md
│   ├── verified-auditors.json
│   ├── revoked-auditors.json
│   │
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml
│   │   │
│   │   │  ── AI INFRASTRUCTURE ───────────────────────────────────────────
│   │   ├── 01-ai-failure.yml
│   │   ├── 14-near-miss.yml
│   │   ├── 15‑prompt‑seal.yml
│   │   ├── 16‑model‑weights‑seal.yml
│   │   ├── 17‑dataset‑declaration.yml
│   │   ├── 22‑ai‑output‑sample.yml
│   │   │
│   │   │  ── RESEARCH & KNOWLEDGE ─────────────────────────────────────────
│   │   ├── 02-research-priority.yml
│   │   ├── 08-foresight-seal.yml
│   │   │
│   │   │  ── EVIDENCE & LEGAL ──────────────────────────────────────────────
│   │   ├── 03-evidence-chain.yml
│   │   ├── 06-scope-anchor.yml
│   │   ├── 18‑agreement‑seal.yml
│   │   ├── 21‑vulnerability‑timeline.yml
│   │   │
│   │   │  ── CREATIVE & CLINICAL ──────────────────────────────────────────
│   │   ├── 04-creative-priority.yml
│   │   ├── 05-clinical-record.yml
│   │   │
│   │   │  ── GENERAL & GOVERNANCE ────────────────────────────────────────
│   │   ├── 07-general-trace.yml
│   │   ├── 09-webeater-link.yml
│   │   ├── 10-audit-request.yml
│   │   ├── 11-audit-completion.yml
│   │   ├── 12-audit-application.yml
│   │   ├── 13-integrity-violation.yml
│   │   ├── 19‑release‑seal.yml
│   │   └── 20‑decision‑record.yml
│   │
│   └── workflows/
│       ├── python-publish.yml
│       ├── auto-seal.yml
│       └── audit-verify.yml
│
│
│  ── ASSETS ──────────────────────────────────────────────────────────────
│
├── assets/
│   │
│   ├── img/
│   │   ├── aion-logo.jpg
│   │   └── favicon.svg
│   │
│   ├── badges/
│   │   │
│   │   ├── sovereign-certified/
│   │   │   ├── sovereign-certified-badge-v2.svg
│   │   │   ├── sovereign-certified-badge-snapshot-v1.svg
│   │   │   ├── sovereign-certified-badge-digital-v2.svg
│   │   │   ├── sovereign-certified-badge-elite-v2.svg
│   │   │   ├── sovereign-certified-badge-defense-v2.svg
│   │   │   └── sovereign-certified-badge-sovereign-v1.svg
│   │   │
│   │   ├── stp_auditor/
│   │   │   ├── stp_auditor_badge_sheldon_v1.svg
│   │   │   ├── stp_auditor_template_v1.svg
│   │   │   └── stp_senior_auditor_template_v1.svg
│   │   │
│   │   ├── compliance/
│   │   │   ├── compliance-constitutional-badge.svg
│   │   │   ├── compliance-finance-badge.svg
│   │   │   ├── compliance-healthcare-badge.svg
│   │   │   └── compliance-legal-badge.svg
│   │   │
│   │   └── verified-simulator/
│   │       ├── aion-verified-simulator-badge-v1.svg
│   │       └── aion-verified-simulator-badge-v2.svg
│   │
│   └── sleeve/
│       ├── big-sleeve/
│       │   ├── aionsystem_auditor_sleeve_bgv1.svg
│       │   ├── aionsystem_certified_audit_sleeve_bgv1.svg
│       │   ├── aionsystem_founders_sleeve_bgv1.svg
│       │   └── aionsystem_sim_verified_sleeve_bgv1.svg
│       │
│       └── small-sleeve/
│           ├── aionsystem_auditor_sleeve_smv1.svg
│           ├── aionsystem_certified_audit_sleeve_smv1.svg
│           ├── aionsystem_founders_sleeve_smv1.svg
│           └── aionsystem_sim_verified_sleeve_smv1.svg
│
│
│  ── CONCEPT ─────────────────────────────────────────────────────────────
│
├── concept/
│   ├── GLOSSARY.md
│   ├── USE-CASES.md
│   ├── DUAL-AUDIENCE-ARCHITECT.md
│   ├── TRUST-WITHOUT-IDENTITY.md
│   ├── PRIOR-ART.md
│   ├── WEBEATER-SPEC.md
│   ├── SUBMISSION-TEMPLATE.md
│   ├── SOVEREIGN-TRACE-v0.1-SPEC.md
│   ├── SOVEREIGN-TRACE-v0.2-SPEC.md
│   ├── SOVEREIGN-TRACE-v0.3-SPEC.md
│   └── SOVEREIGN-TRACE-v0.4-SPEC.md
│
│
│  ── SOVEREIGN TRACE PACKAGE ─────────────────────────────────────────────
│
├── sovereign_trace/
│   ├── __init__.py
│   ├── sovereign_trace_stamp.py          ← FROZEN-4.0 · active
│   ├── FROZEN-4.0-MANIFEST.md
│   │
│   ├── FROZEN-3.0-RETIRED/
│   │   ├── FROZEN-3.0-MANIFEST.md
│   │   └── sovereign-trace-stamp-frozen-3.0-retired.py
│   │
│   ├── FROZEN-2.0-RETIRED/
│   │   ├── FROZEN-2.0-MANIFEST.md
│   │   └── sovereign_trace_stamp-frozen-v2.0-retired.py
│   │
│   └── FROZEN-1.0-RETIRED/
│       ├── FROZEN-1.0-RETIRED.md
│       └── ARCHIVE-EMPTY.md
│
│
│  ── LEDGER — 66 ENTRIES ─────────────────────────────────────────────────
│
├── ledger/
│   │
│   │  ── FOUNDING ENTRIES (March 9–11, 2026) ───────────────────────────
│   ├── STP-GENERAL-TRACE-2026-03-09-000005.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-09-000008.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000006.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000007.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000009.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000010.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000011.json
│   ├── STP-FORESIGHT-SEAL-2026-03-10-000012.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-10-000013.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-10-000014.json
│   ├── STP-FORESIGHT-SEAL-2026-03-11-000015.json
│   │
│   │  ── RESEARCH PRIORITY ────────────────────────────────────────────
│   ├── STP-RESEARCH-PRIORITY-2026-03-14-U3N9CK.json
│   ├── STP-RESEARCH-PRIORITY-March-23-2026-179F5D.json
│   ├── STP-RESEARCH-PRIORITY-March-26-2026-E0EC9D.json
│   │
│   │  ── GENERAL TRACE ────────────────────────────────────────────────
│   ├── STP-GENERAL-TRACE-March-24-2026-03C2A9.json
│   ├── STP-GENERAL-TRACE-March-24-2026-CE0CDF.json
│   ├── STP-GENERAL-TRACE-March-25-2026-3A0CDF.json
│   ├── STP-GENERAL-TRACE-March-25-2026-5496D4.json
│   ├── STP-GENERAL-TRACE-March-25-2026-997E9E.json
│   ├── STP-GENERAL-TRACE-March-25-2026-D04983.json
│   ├── STP-GENERAL-TRACE-March-25-2026-EED151.json
│   ├── STP-GENERAL-TRACE-March-26-2026-8A049A.json
│   ├── STP-GENERAL-TRACE-March-27-2026-AFCE36.json
│   ├── STP-GENERAL-TRACE-March-31-2026-028FF7.json
│   ├── STP-GENERAL-TRACE-March-31-2026-1A3C1A.json
│   ├── STP-GENERAL-TRACE-March-31-2026-1DE84E.json
│   ├── STP-GENERAL-TRACE-March-31-2026-220109.json
│   ├── STP-GENERAL-TRACE-March-31-2026-3B5639.json
│   ├── STP-GENERAL-TRACE-March-31-2026-4B6F0F.json
│   ├── STP-GENERAL-TRACE-March-31-2026-4DE8F8.json
│   ├── STP-GENERAL-TRACE-March-31-2026-550742.json
│   ├── STP-GENERAL-TRACE-March-31-2026-56BD1E.json
│   ├── STP-GENERAL-TRACE-March-31-2026-58E302.json
│   ├── STP-GENERAL-TRACE-March-31-2026-63C102.json
│   ├── STP-GENERAL-TRACE-March-31-2026-68B4A6.json
│   ├── STP-GENERAL-TRACE-March-31-2026-69DD5F.json
│   ├── STP-GENERAL-TRACE-March-31-2026-70EDAF.json
│   ├── STP-GENERAL-TRACE-March-31-2026-7D5DAE.json
│   ├── STP-GENERAL-TRACE-March-31-2026-964A6F.json
│   ├── STP-GENERAL-TRACE-March-31-2026-A51FEA.json
│   ├── STP-GENERAL-TRACE-March-31-2026-AFE44D.json
│   ├── STP-GENERAL-TRACE-March-31-2026-B08FFC.json
│   ├── STP-GENERAL-TRACE-March-31-2026-BDCE58.json
│   ├── STP-GENERAL-TRACE-March-31-2026-BFAF9E.json
│   ├── STP-GENERAL-TRACE-March-31-2026-C8B202.json
│   ├── STP-GENERAL-TRACE-March-31-2026-EE2D54.json
│   ├── STP-GENERAL-TRACE-March-31-2026-F5DBAD.json
│   ├── STP-GENERAL-TRACE-April-1-2026-0D8223.json
│   ├── STP-GENERAL-TRACE-April-1-2026-C49B22.json
│   │
│   │  ── CREATIVE PRIORITY ────────────────────────────────────────────
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-2A3BAF.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-4A5EF0.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-8B1D2E.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-E9C306.json
│   │
│   │  ── EVIDENCE CHAIN ──────────────────────────────────────────────
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-0794A2.json
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-3B7DE3.json
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-8ABB30.json
│   ├── STP-EVIDENCE-CHAIN-March-25-2026-D0D735.json
│   │
│   │  ── SCOPE ANCHOR ────────────────────────────────────────────────
│   ├── STP-SCOPE-ANCHOR-March-24-2026-386FB6.json
│   ├── STP-SCOPE-ANCHOR-March-24-2026-60B407.json
│   ├── STP-SCOPE-ANCHOR-March-25-2026-557510.json
│   ├── STP-SCOPE-ANCHOR-March-25-2026-A10666.json
│   │
│   │  ── CLINICAL RECORD ─────────────────────────────────────────────
│   ├── STP-CLINICAL-RECORD-March-25-2026-343075.json
│   ├── STP-CLINICAL-RECORD-March-25-2026-91F0E9.json
│   │
│   │  ── WEBEATER LINK ───────────────────────────────────────────────
│   ├── STP-WEBEATER-LINK-March-25-2026-5989D1.json
│   ├── STP-WEBEATER-LINK-March-25-2026-E43621.json
│   │
│   │  ── INTEGRITY VIOLATION ─────────────────────────────────────────
│   ├── STP-INTEGRITY-VIOLATION-March-27-2026-3B5F2D.json
│   └── STP-INTEGRITY-VIOLATION-March-27-2026-ACD8A4.json
│
│
│  ── TEST SUITE — 30 SUITES ──────────────────────────────────────────────
│
└── tests/
    ├── conftest.py
    │
    │  ── CALENDAR VERIFICATION ────────────────────────────────────────
    ├── test_gregorian.py
    ├── test_hebrew_calendar.py
    ├── test_hebrew_anchors.py
    ├── test_hebrew_edge_cases.py
    ├── test_dreamspell_calendar.py
    ├── test_jd_bridge.py
    │
    │  ── STAMP CORE ──────────────────────────────────────────────────
    ├── test_stamp_core.py
    ├── test_stamp_and_record.py
    ├── test_stamp_batch.py
    ├── test_stamp_normalization.py
    ├── test_stamp_datetime_handling.py
    ├── test_stamp_error_handling.py
    │
    │  ── CLASS CONTRACTS ─────────────────────────────────────────────
    ├── test_sovereign_stamp_class.py
    ├── test_sovereign_record_class.py
    │
    │  ── VERIFICATION & DISPLAY ──────────────────────────────────────
    ├── test_verify.py
    ├── test_verify_result.py
    ├── test_display.py
    ├── test_serialization.py
    │
    │  ── INTEGRITY & REGRESSION ──────────────────────────────────────
    ├── test_file_integrity.py
    ├── test_frozen_version.py
    ├── test_backward_compat.py
    ├── test_regression.py
    ├── test_properties.py
    │
    │  ── PERFORMANCE & CONCURRENCY ───────────────────────────────────
    ├── test_performance.py
    ├── test_concurrency.py
    ├── test_async_stamp.py
    │
    │  ── INTERFACE ───────────────────────────────────────────────────
    ├── test_cli.py
    ├── test_package_imports.py
    ├── test_self_test_runner.py
    │
    └── REPORTS/
        └── [per-suite report directory — one per test file]
```

---

<div align="center">

## Ledger Summary

[![General Trace](https://img.shields.io/badge/GENERAL%20TRACE-43%20entries-546E7A?style=flat-square)](./ledger/)
[![Creative Priority](https://img.shields.io/badge/CREATIVE%20PRIORITY-7%20entries-7B1FA2?style=flat-square)](./ledger/)
[![Evidence Chain](https://img.shields.io/badge/EVIDENCE%20CHAIN-4%20entries-1565C0?style=flat-square)](./ledger/)
[![Scope Anchor](https://img.shields.io/badge/SCOPE%20ANCHOR-4%20entries-00695C?style=flat-square)](./ledger/)
[![Research Priority](https://img.shields.io/badge/RESEARCH%20PRIORITY-3%20entries-E65100?style=flat-square)](./ledger/)
[![Foresight Seal](https://img.shields.io/badge/FORESIGHT%20SEAL-2%20entries-F57F17?style=flat-square)](./ledger/)
[![Clinical Record](https://img.shields.io/badge/CLINICAL%20RECORD-2%20entries-B71C1C?style=flat-square)](./ledger/)
[![Webeater Link](https://img.shields.io/badge/WEBEATER%20LINK-2%20entries-00838F?style=flat-square)](./ledger/)
[![Integrity Violation](https://img.shields.io/badge/INTEGRITY%20VIOLATION-2%20entries-D50000?style=flat-square)](./ledger/)

**66 sealed entries · March 9 – April 1, 2026**

</div>

---

<div align="center">

## Test Coverage

[![Calendar](https://img.shields.io/badge/CALENDAR-6%20suites-0288D1?style=flat-square)](./tests/)
[![Stamp Core](https://img.shields.io/badge/STAMP%20CORE-6%20suites-2E7D32?style=flat-square)](./tests/)
[![Class Contracts](https://img.shields.io/badge/CLASS%20CONTRACTS-2%20suites-4527A0?style=flat-square)](./tests/)
[![Verification](https://img.shields.io/badge/VERIFICATION-4%20suites-00695C?style=flat-square)](./tests/)
[![Integrity](https://img.shields.io/badge/INTEGRITY-5%20suites-E65100?style=flat-square)](./tests/)
[![Performance](https://img.shields.io/badge/PERFORMANCE-3%20suites-F57F17?style=flat-square)](./tests/)
[![Interface](https://img.shields.io/badge/INTERFACE-3%20suites-546E7A?style=flat-square)](./tests/)

**30 test suites · 82 self-test checks passing · FROZEN-4.0**

</div>

---

<div align="center">

*Sovereign Trace Protocol — AionSystem*
*Author: Sheldon K. Salmon — AI Reliability & AGI Architect*

[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--8057--5115-a6ce39?style=flat&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-8057-5115)
[![DOI](https://zenodo.org/badge/1174130098.svg)](https://doi.org/10.5281/zenodo.18941392)

</div>
