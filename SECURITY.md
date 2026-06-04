# SECURITY POLICY

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & ADI/AGI Architect

---

## SUPPORTED VERSIONS

| Version | Status | Security Support |
|---------|--------|-----------------|
| 4.0.0 (FROZEN-4.0) | Current | Active |
| 3.x (FROZEN-3.0) | Retired | None — see FROZEN declaration |
| 2.x (FROZEN-2.0) | Retired | None — see FROZEN declaration |
| 1.x (FROZEN-1.0) | Retired | None — see FROZEN declaration |

FROZEN-1.0, FROZEN-2.0, and FROZEN-3.0 are retired and receive no security support.
Do not use them for new stamp production. See `stamp/FROZEN-X.0-RETIRED/` for archives.

---

## SCOPE

Security vulnerabilities relevant to this project include:

**In scope:**
- Weaknesses in the SHA-256 seal computation that could allow
  undetected modification of a sealed entry
- Collision vulnerabilities in the seal payload construction
  (e.g., two different inputs producing the same seal)
- Bypass of the `verify()` function's tamper detection
- Logic errors in the Hebrew, Gregorian, or Dreamspell calendar
  algorithms that could cause two different dates to produce
  the same representation (calendar collision)
- Dependency vulnerabilities in the Python standard library
  functions used (`hashlib`, `json`, `datetime`)

**Out of scope:**
- Vulnerabilities in Python itself or its standard library
  (report these to https://python.org/dev/security/)
- General cryptographic weaknesses in SHA-256 at the algorithm
  level (SHA-256 preimage and collision resistance are managed
  by NIST — report to https://csrc.nist.gov)
- Social engineering, phishing, or attacks targeting users
  rather than the software
- Theoretical attacks requiring quantum computing capability
  not currently available

---

## REPORTING A VULNERABILITY

**Do not open a public GitHub issue for security vulnerabilities.**

Security vulnerabilities must be reported privately.

**How to report:**

1. Send a detailed report to the repository via GitHub's
   private security advisory feature:
   `https://github.com/AionSystem/SOVEREIGN-TRACE-PROTOCOL/security/advisories/new`

2. Include in your report:
   - Description of the vulnerability
   - Steps to reproduce
   - Affected versions
   - Potential impact assessment
   - If known, suggested remediation

**Response commitment:**

| Milestone | Target |
|-----------|--------|
| Acknowledgment of receipt | 72 hours |
| Initial assessment | 7 days |
| Resolution decision | 30 days |
| Public disclosure | Coordinated — after fix deployed or 90 days, whichever comes first |

---

## FROZEN CODE AND SECURITY FIXES

`stamp/sovereign_trace_stamp.py` (FROZEN-4.0) is permanently immutable
by architectural declaration. If a security vulnerability is confirmed
in FROZEN-4.0:

1. FROZEN-4.0 will be **retired** — moved to `stamp/FROZEN-4.0-RETIRED/`
2. A **DEFECT-RECORD.md** will document the vulnerability publicly
3. **FROZEN-5.0** will be built from first principles incorporating
   the fix, verified against all anchor cases, and deployed
4. Users of FROZEN-4.0 will be notified via a GitHub security advisory
5. All stamps produced by FROZEN-4.0 prior to retirement remain
   valid under FROZEN-4.0 semantics but carry the defect notation

This process cannot be shortened. The FROZEN declaration is
architectural. It is also what makes the stamp trustworthy.
A frozen function that patches itself is not frozen.

---

## RESPONSIBLE DISCLOSURE POLICY

The author follows coordinated vulnerability disclosure. We request:

- Private notification before public disclosure
- Reasonable time to develop and deploy a fix before publication
- No exploitation of vulnerabilities in ways that affect users

In return, we commit to:

- Prompt acknowledgment and transparent communication
- Credit to the reporter in the security advisory (unless anonymity
  is requested)
- No legal action against good-faith security researchers acting
  within this policy

---

## SAFE HARBOR

We consider security research conducted in good faith and in
accordance with this policy to be authorized. We will not pursue
legal action against researchers who:

- Discover and privately report a genuine security vulnerability
- Make a good faith effort to avoid harm to users
- Do not access, modify, or exfiltrate data beyond what is
  necessary to demonstrate the vulnerability
- Do not engage in actions that could impact availability of the
  repository or PyPI package

---

*Sovereign Trace Protocol — SECURITY.md*
*Author: Sheldon K. Salmon — AI Reliability & ADI/AGI Architect | June 2026*
