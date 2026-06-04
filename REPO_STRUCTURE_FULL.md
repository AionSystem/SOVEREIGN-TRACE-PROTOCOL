<div align="center">

# SOVEREIGN TRACE PROTOCOL — FULL REPOSITORY STRUCTURE

**Complete file manifest · FROZEN-4.0 · June 2026**

[![Permanent](https://img.shields.io/badge/PERMANENT-FROZEN--4.0-2E7D32?style=flat-square&logo=git&logoColor=white)](https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL)
[![PyPI](https://img.shields.io/pypi/v/sovereign-trace?style=flat-square&color=2E7D32&label=PyPI)](https://pypi.org/project/sovereign-trace/)
[![Dependencies](https://img.shields.io/badge/DEPS-stdlib%20only-616161?style=flat-square)](https://docs.python.org/3/library/index.html)
[![Tests](https://img.shields.io/badge/TESTS-30%20suites-1565C0?style=flat-square&logo=pytest&logoColor=white)](./tests/)
[![Ledger](https://img.shields.io/badge/LEDGER-66%20entries-4527A0?style=flat-square&logo=hashnode&logoColor=white)](./ledger/)
[![Templates](https://img.shields.io/badge/TEMPLATES-31%20issue%20types-0288D1?style=flat-square)](./ISSUE_TEMPLATE/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-darkgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: Commercial](https://img.shields.io/badge/License-Commercial-orange.svg)](./LICENSE-COMMERCIAL.md)
[![Legal Posture](https://img.shields.io/badge/LEGAL-Posture%20Active-8B0000?style=flat-square)](./LEGAL-POSTURE.md)

</div>

Complete list of all folders and files in the repository.

## Directory and File Tree

```
/workspace
├── .coveragerc
├── .git
│   ├── HEAD
│   ├── branches
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   ├── refs
│   │   │   ├── heads
│   │   │   │   ├── MASTER
│   │   │   │   └── qwen-code-d02b70aa-dca4-45b5-9b3d-c9d65d840e20
│   │   │   └── remotes
│   │   │       └── origin
│   │   │           └── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   ├── MASTER
│   │       │   └── qwen-code-d02b70aa-dca4-45b5-9b3d-c9d65d840e20
│   │       └── remotes
│   │           └── origin
│   │               └── HEAD
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │       ├── pack-48de56d00b41b4c248e74a0c670cafdb6f2cd977.idx
│   │       └── pack-48de56d00b41b4c248e74a0c670cafdb6f2cd977.pack
│   ├── packed-refs
│   ├── refs
│   │   ├── heads
│   │   │   ├── MASTER
│   │   │   └── qwen-code-d02b70aa-dca4-45b5-9b3d-c9d65d840e20
│   │   ├── remotes
│   │   │   └── origin
│   │   │       └── HEAD
│   │   └── tags
│   └── shallow
├── .github
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE
│   │   ├── 00-feedback.yml
│   │   ├── 01-ai-failure.yml
│   │   ├── 02-research-priority.yml
│   │   ├── 03-evidence-chain.yml
│   │   ├── 04-creative-priority.yml
│   │   ├── 05-clinical-record.yml
│   │   ├── 06-scope-anchor.yml
│   │   ├── 07-general-trace.yml
│   │   ├── 08-foresight-seal.yml
│   │   ├── 09-webeater-link.yml
│   │   ├── 10-audit-request-snapshot.yml
│   │   ├── 10-audit-request-tier1-5.yml
│   │   ├── 11-audit-completion.yml
│   │   ├── 12-audit-application.yml
│   │   ├── 13-integrity-violation.yml
│   │   ├── 14-near-miss.yml
│   │   ├── 15‑prompt‑seal.yml
│   │   ├── 16‑model‑weights‑seal.yml
│   │   ├── 17‑dataset‑declaration.yml
│   │   ├── 18‑agreement‑seal.yml
│   │   ├── 19‑release‑seal.yml
│   │   ├── 20‑decision‑record.yml
│   │   ├── 21‑vulnerability‑timeline.yml
│   │   ├── 22‑ai‑output‑sample.yml
│   │   ├── 23-Bias-Audit-Record.yml
│   │   ├── 24-Red-Team-Engagement.yml
│   │   ├── 25-Model-Card-Seal.yml
│   │   ├── 26-Human-Oversight-Log.yml
│   │   ├── 27-Code-Snippet-Seal.yml
│   │   ├── 28-Research-Logbook.yml
│   │   ├── 29-Identity-Anchor.yml
│   │   ├── 30-Temporal-Commitment.yml
│   │   └── config.yml
│   ├── SECURITY.md
│   ├── actions
│   │   └── stp-seal
│   │       └── action.yml
│   ├── bad_actors.yml
│   ├── revoked-auditors.json
│   ├── verified-auditors.json
│   └── workflows
│       ├── abuse-detector.yml
│       ├── blockchain-anchor.yml
│       ├── python-publish.yml
│       ├── sovereign-trace-audit-verify.yml
│       └── sovereign-trace-auto-seal.yml
├── .gitignore
├── .safety-policy.yml
├── ACCEPTABLE-USE-POLICY.md
├── AI-ETHICS-STATEMENT.md
├── AUDIT-METHODOLOGY.md
├── AUDITOR-VETTING-PROCESS.md
├── CERTIFICATION.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTOR-LICENSE-AGREEMENT.md
├── CONTRIBUTOR-TERMS.md
├── DATA-PROCESSING-AGREEMENT.md
├── DISASTER-RECOVERY.md
├── EPISTEMIC-DEBT-SCORE.md
├── EXPORT-CONTROL.md
├── HOW-TO-SUBMIT.md
├── LEGAL-POSTURE.md
├── LICENSE
├── LICENSE-COMMERICAL.md
├── LICENSE-EXPLANATION.md
├── LICENSE-GPLv3.md
├── METHODOLOGY.md
├── MUTUAL-NDA.md
├── NON-RECOURSE-STATEMENT.md
├── NOTICE
├── PATENTS.md
├── PRINCIPLES.md
├── PRIVACY-POLICY.md
├── QUICKSTART.md
├── README.md
├── REPO_STRUCTURE.md
├── SECURITY-INSIGHTS.yml
├── SECURITY.md
├── STANDARDS-ALIGNMENT.md
├── STP-logo.svg
├── TERMS OF SERVICE.md
├── TRADEMARK-USAGE-POLICY.md
├── TRADEMARK.md
├── UNILATERAL-NDA.md
├── assets
│   ├── badges
│   │   ├── compliance
│   │   │   ├── compliance-constitutional-badge.svg
│   │   │   ├── compliance-finance-badge.svg
│   │   │   └── compliance-healthcare-badge.svg
│   │   ├── personal-cert
│   │   │   ├── capc-badge-matrix-v1.svg
│   │   │   └── sacs-badge-personal-v1.svg
│   │   ├── sovereign-certified
│   │   │   ├── sovereign-certified-badge-defense-v2.svg
│   │   │   ├── sovereign-certified-badge-digital-v2.svg
│   │   │   ├── sovereign-certified-badge-elite-v2.svg
│   │   │   ├── sovereign-certified-badge-snapshot-v1.svg
│   │   │   ├── sovereign-certified-badge-sovereign-v1.svg
│   │   │   └── sovereign-certified-badge-v2.svg
│   │   ├── stp_auditor
│   │   │   ├── stp_auditor_badge_beginner.svg
│   │   │   ├── stp_auditor_badge_senior.svg
│   │   │   ├── stp_auditor_badge_sheldon_v1.svg
│   │   │   └── stp_auditor_badge_standard.svg
│   │   └── verified-simulator
│   │       ├── aion-verified-simulator-badge-v1.svg
│   │       └── aion-verified-simulator-badge-v2.svg
│   ├── img
│   │   ├── aion-logo.jpg
│   │   └── favicon.svg
│   └── sleeve
│       ├── big-sleeve
│       │   ├── aionsystem_auditor_sleeve_bgv1.svg
│       │   ├── aionsystem_capc_professional_sleeve_bgv1.svg
│       │   ├── aionsystem_certified_audit_sleeve_bgv1.svg
│       │   ├── aionsystem_founders_sleeve_bgv1.svg
│       │   ├── aionsystem_sacs_personal_sleeve_bgv1.svg
│       │   └── aionsystem_sim_verified_sleeve_bgv1.svg
│       ├── mock
│       │   └── aionsystem_certified_audit_sleeve_mock_nexus.svg
│       └── small-sleeve
│           ├── aionsystem_auditor_sleeve_smv1.svg
│           ├── aionsystem_capc_professional_sleeve_smv1.svg
│           ├── aionsystem_certified_audit_sleeve_smv1.svg
│           ├── aionsystem_founders_sleeve_smv1.svg
│           ├── aionsystem_sacs_personal_sleeve_smv1.svg
│           └── aionsystem_sim_verified_sleeve_smv1.svg
├── chaos
│   └── experiment.json
├── concept
│   ├── DUAL-AUDIENCE-ARCHITECT.md
│   ├── GLOSSARY.md
│   ├── PRIOR-ART.md
│   ├── SOVEREIGN-TRACE-v0.1-SPEC.md
│   ├── SOVEREIGN-TRACE-v0.2-SPEC.md
│   ├── SOVEREIGN-TRACE-v0.3-SPEC.md
│   ├── SOVEREIGN-TRACE-v0.4-SPEC.md
│   ├── SUBMISSION-TEMPLATE.md
│   ├── TRUST-WITHOUT-IDENTITY.md
│   ├── USE-CASES.md
│   └── WEBEATER-SPEC.md
├── ledger
│   ├── STP-CLINICAL-RECORD-March-25-2026-343075.json
│   ├── STP-CLINICAL-RECORD-March-25-2026-91F0E9.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-09-000008.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-10-000013.json
│   ├── STP-CREATIVE-PRIORITY-2026-03-10-000014.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-2A3BAF.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-4A5EF0.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-8B1D2E.json
│   ├── STP-CREATIVE-PRIORITY-March-24-2026-E9C306.json
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-0794A2.json
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-3B7DE3.json
│   ├── STP-EVIDENCE-CHAIN-March-24-2026-8ABB30.json
│   ├── STP-EVIDENCE-CHAIN-March-25-2026-D0D735.json
│   ├── STP-FORESIGHT-SEAL-2026-03-10-000012.json
│   ├── STP-FORESIGHT-SEAL-2026-03-11-000015.json
│   ├── STP-GENERAL-TRACE-2026-03-09-000005.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000006.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000007.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000009.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000010.json
│   ├── STP-GENERAL-TRACE-2026-03-10-000011.json
│   ├── STP-GENERAL-TRACE-April-1-2026-0D8223.json
│   ├── STP-GENERAL-TRACE-April-1-2026-C49B22.json
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
│   ├── STP-INTEGRITY-VIOLATION-March-27-2026-3B5F2D.json
│   ├── STP-INTEGRITY-VIOLATION-March-27-2026-ACD8A4.json
│   ├── STP-RESEARCH-PRIORITY-2026-03-14-U3N9CK.json
│   ├── STP-RESEARCH-PRIORITY-March-23-2026-179F5D.json
│   ├── STP-RESEARCH-PRIORITY-March-26-2026-E0EC9D.json
│   ├── STP-SCOPE-ANCHOR-March-24-2026-386FB6.json
│   ├── STP-SCOPE-ANCHOR-March-24-2026-60B407.json
│   ├── STP-SCOPE-ANCHOR-March-25-2026-557510.json
│   ├── STP-SCOPE-ANCHOR-March-25-2026-A10666.json
│   ├── STP-WEBEATER-LINK-March-25-2026-5989D1.json
│   └── STP-WEBEATER-LINK-March-25-2026-E43621.json
├── pyproject.toml
├── pytest.ini
├── scripts
│   ├── migrate_ledger_to_hierarchy.py
│   ├── stp_abuse_detector.py
│   └── stp_blockchain_anchor.py
├── sovereign_trace
│   ├── FROZEN-1.0-RETIRED
│   │   ├── ARCHIVE-EMPTY.md
│   │   └── FROZEN-1.0-RETIRED.md
│   ├── FROZEN-2.0-RETIRED
│   │   ├── FROZEN-2.0-MANIFEST.md
│   │   └── sovereign_trace_stamp-frozen-v2.0-retired.py
│   ├── FROZEN-3.0-RETIRED
│   │   ├── FROZEN-3.0-MANIFEST.md
│   │   └── sovereign-trace-stamp-frozen-3.0-retired.py
│   ├── FROZEN-4.0-MANIFEST.md
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── sovereign_trace_stamp.cpython-312.pyc
│   └── sovereign_trace_stamp.py
├── tests
│   ├── REPORTS
│   │   ├── test_async_stamp
│   │   │   └── placeholder.md
│   │   ├── test_backward_compat
│   │   │   └── placeholder.md
│   │   ├── test_cli
│   │   │   └── placeholder.md
│   │   ├── test_concurrency
│   │   │   └── placeholder.md
│   │   ├── test_display
│   │   │   └── placeholder.md
│   │   ├── test_dreamspell_calendar
│   │   │   └── placeholder.md
│   │   ├── test_file_integrity
│   │   │   └── placeholder.md
│   │   ├── test_frozen_version
│   │   │   └── placeholder.md
│   │   ├── test_gregorian
│   │   │   └── placeholder.md
│   │   ├── test_hebrew_anchors
│   │   │   └── placeholder.md
│   │   ├── test_hebrew_calendar
│   │   │   └── placeholder.md
│   │   ├── test_hebrew_edge_cases
│   │   │   └── placeholder.md
│   │   ├── test_jd_bridge
│   │   │   └── placeholder.md
│   │   ├── test_package_imports
│   │   │   └── placeholder.md
│   │   ├── test_performance
│   │   │   └── placeholder.md
│   │   ├── test_properties
│   │   │   └── placeholder.md
│   │   ├── test_regression
│   │   │   └── placeholder.md
│   │   ├── test_self_test_runner
│   │   │   └── placeholder.md
│   │   ├── test_serialization
│   │   │   └── placeholder.md
│   │   ├── test_sovereign_record_class
│   │   │   └── placeholder.md
│   │   ├── test_sovereign_stamp_class
│   │   │   └── placeholder.md
│   │   ├── test_stamp_and_record
│   │   │   └── placeholder.md
│   │   ├── test_stamp_batch
│   │   │   └── placeholder.md
│   │   ├── test_stamp_core
│   │   │   └── placeholder.md
│   │   ├── test_stamp_datetime_handling
│   │   │   └── placeholder.md
│   │   ├── test_stamp_error_handling
│   │   │   └── placeholder.md
│   │   ├── test_stamp_normalization
│   │   │   └── placeholder.md
│   │   ├── test_verify
│   │   │   └── placeholder.md
│   │   └── test_verify_result
│   │       └── placeholder.md
│   ├── __pycache__
│   │   ├── conftest.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_backward_compat.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_cli.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_display.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_dreamspell_calendar.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_frozen_version.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_gregorian.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_hebrew_anchors.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_hebrew_calendar.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_hebrew_edge_cases.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_jd_bridge.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_package_imports.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_regression.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_serialization.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_sovereign_record_class.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_sovereign_stamp_class.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_and_record.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_batch.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_core.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_datetime_handling.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_error_handling.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_stamp_normalization.cpython-312-pytest-9.0.3.pyc
│   │   ├── test_verify.cpython-312-pytest-9.0.3.pyc
│   │   └── test_verify_result.cpython-312-pytest-9.0.3.pyc
│   ├── conftest.py
│   ├── fuzz
│   │   └── fuzz_stamp.py
│   ├── test_async_stamp.py
│   ├── test_backward_compat.py
│   ├── test_cli.py
│   ├── test_concurrency.py
│   ├── test_display.py
│   ├── test_dreamspell_calendar.py
│   ├── test_file_integrity.py
│   ├── test_frozen_version.py
│   ├── test_gregorian.py
│   ├── test_hebrew_anchors.py
│   ├── test_hebrew_calendar.py
│   ├── test_hebrew_edge_cases.py
│   ├── test_jd_bridge.py
│   ├── test_package_imports.py
│   ├── test_performance.py
│   ├── test_properties.py
│   ├── test_regression.py
│   ├── test_self_test_runner.py
│   ├── test_serialization.py
│   ├── test_sovereign_record_class.py
│   ├── test_sovereign_stamp_class.py
│   ├── test_stamp_and_record.py
│   ├── test_stamp_batch.py
│   ├── test_stamp_core.py
│   ├── test_stamp_datetime_handling.py
│   ├── test_stamp_error_handling.py
│   ├── test_stamp_normalization.py
│   ├── test_verify.py
│   └── test_verify_result.py
└── tox.ini
```

## Summary Statistics

- **Total Directories**: Counted from tree above
- **Total Files**: Counted from tree above
- **Generated**: This file was auto-generated with full repository structure

---
*This document contains the complete directory and file listing for the entire repository.*
