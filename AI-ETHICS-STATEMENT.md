# AI ETHICS STATEMENT

**Sovereign Trace Protocol**
**Author:** Sheldon K. Salmon — AI Reliability & ADI/AGI Architect
**Version:** 1.1 | Effective: June 2026
**Supersedes:** Version 1.0 (March 2026)

**Change log for v1.1:**
- Added expanded prohibited uses (fraud, forgery, intentional deception)
- Clarified network call claim: offline stamp vs. optional GitHub Actions
- Added future‑law caveat for AI authorship
- Added explanation of certification rewards (badge, registry)
- Added mention of FRAGILE_VALID / TOPOLOGICALLY_ISOLATED certification warnings
- Added third‑party reporting mechanism
- Added annual review commitment
- Added note about GitHub data retention for optional workflow
- Added jurisdiction conflict clause
- Corrected author title

---

## STATEMENT OF POSITION

The Sovereign Trace Protocol is built by an AI Reliability & ADI/AGI Architect
who works at the intersection of AI systems and human epistemic sovereignty.
This statement declares the ethical principles that govern the design,
deployment, and certification activities of this protocol.

This is not a marketing document. It is an operational commitment.
Every clause below is reflected in architectural decisions in the codebase,
the certification methodology, and the legal structure of this repository.

---

## 1. HONESTY BEFORE PERFORMANCE

AI systems that appear reliable are more dangerous than AI systems that
are known to fail. The performance of reliability — dashboards that show
green, outputs that sound confident, error rates that go unreported —
is the primary failure mode in deployed AI today.

The Sovereign Trace Protocol is built on the opposite principle:
an honest record of failures is more valuable than a clean record
that conceals them. The certification framework rewards organizations
that build infrastructure to capture failures honestly — not those
that minimize the appearance of failure.

**Rewards for honest organisations include:**
- Listing in the public **Trust Registry** (`AionSystem/TRUST-REGISTRY`)
- Issuance of a **Sovereign Certified badge** (displayable publicly)
- The ability to reference the certification in procurement and compliance contexts

**Architectural expression:** The Trust Registry is a public record.
Remediated failures are permanent entries. There is no mechanism
to delete a failure from the record. A remediation does not erase
what was remediated.

---

## 2. HUMAN AUTHORSHIP AND AI TOOLS

AI tools were used in the development of this protocol.
Claude (Anthropic) assisted with code drafting, documentation,
and framework specification under the direction and review of
Sheldon K. Salmon.

This assistance is disclosed — not concealed. The author takes
full creative and technical responsibility for all outputs.
AI assistance does not create AI authorship. Every decision
about what to include, what to change, and what to ship
was made by the human architect.

The author holds no position that AI tools are incapable of
meaningful contribution. The author holds the position that
contribution and authorship are different things, and that
honest disclosure of AI assistance is the minimum standard
for any work that will be used in commercial, legal,
or high-stakes contexts.

**Forward‑looking caveat:** This statement reflects current law
(United States, European Union, United Kingdom) as of June 2026.
If future legal changes grant AI authorship, the author will update
this statement accordingly. The underlying principle — that the
human architect takes full responsibility — remains unchanged.

**Architectural expression:** `NOTICE` discloses AI tool use
explicitly. `PRINCIPLES.md` analyzes AI authorship under
applicable law across multiple jurisdictions.

---

## 3. EPISTEMIC INTEGRITY

The author developed the AION Constitutional Stack — a framework
architecture for measuring and managing AI reliability. A core
principle of that stack is epistemic integrity: the obligation
to report the actual state of confidence in any claim, not the
state that would be most persuasive or most commercially convenient.

This protocol applies that principle to itself:

- Unvalidated claims are tagged `[?]` — not presented as established
- Convergence states are declared honestly (M-NASCENT = specified
  but not yet validated in production)
- The core hypothesis — that significance hunger resolves at the
  moment of stamping — is explicitly marked as unverified pending
  real-world FCL data
- No framework in the AION stack is presented as more validated
  than it actually is

**Architectural expression:** ECF tagging throughout all
specification documents. Convergence state register in `README.md`.

---

## 4. INDIVIDUAL SOVEREIGNTY OVER DATA

The Sovereign Trace Protocol is designed so that the individual
retains full control over their trace records at all times.

- No central server holds trace entries
- No platform dependency — the stamp function runs locally
- No account required — `pip install sovereign-trace` and stamp
- The JSON record is yours: store it wherever you choose
- No vendor can delete, modify, or access your records

**Important clarification:** The stamp function `sovereign_trace_stamp.py`
makes **no network calls** and runs entirely offline. The optional
GitHub Actions workflows (auto‑seal, abuse detector, blockchain anchor)
**do** make network calls to GitHub’s infrastructure and are opt‑in.
If you use the GitHub Issues workflow, your trace entries are stored
on GitHub’s servers and subject to GitHub’s privacy policy and terms
of service. The offline stamp function avoids this entirely.

This is not a privacy policy. It is a design commitment:
sovereignty is not a feature. It is the architecture.

**Architectural expression:** `sovereign_trace_stamp.py` is
zero-dependency, runs entirely locally, produces portable JSON.
No network call is made during stamp generation. Ever.

---

## 5. PROHIBITED USES (Expanded from Anti‑Weaponization)

The Sovereign Trace Protocol may not be used for any of the following:

- Creating surveillance infrastructure, stalking tools, or any mechanism
  designed to harm individuals
- **Timestamping false or misleading information with the intent to deceive**
  (using the seal to lend credibility to a lie)
- Fraud, forgery, or fabrication of evidence
- Money laundering, sanctions evasion, or any other financial crime
- Human rights abuses, including but not limited to:
  - Arbitrary detention
  - Denial of due process
  - Surveillance of journalists, activists, or human rights defenders
  - Enforced disappearance
- Any use that violates the laws of the user’s jurisdiction

The triple-time stamp is designed to register what is true.
It is not designed to manufacture the appearance of what is true.
Using the seal to create false records, back-dated entries,
or fabricated audit trails inverts the protocol's purpose.

Such use violates the Acceptable Use Policy (`ACCEPTABLE-USE-POLICY.md`)
and constitutes grounds for immediate license termination.

---

## 6. ACCOUNTABILITY WITHOUT PUNISHMENT

The certification framework is built to create accountability —
not to punish organizations for having AI failures.

AI systems fail. The question is not whether an organization's
AI fails but whether they have infrastructure that captures
failures honestly and remediates them transparently.

An organization with a certified deployment and a documented
failure history is not a bad organization. It is an honest one.
The certification framework rewards honesty. It does not reward
the concealment of failures.

**Certification warnings:** Some certifications (e.g., `FRAGILE_VALID`
or `TOPOLOGICALLY_ISOLATED`) explicitly warn of structural weaknesses;
they do not imply system safety or reliability. These statuses are
disclosed in the certification statement and the Trust Registry.

**Architectural expression:** Tier 1 Basic Verification is
deliberately designed around the premise that an organization
already has a failure to report. The entry point to certification
is a remediated failure — not a clean record.

---

## 7. NO ENDORSEMENT OF SPECIFIC AI SYSTEMS

The Sovereign Trace Protocol does not endorse, recommend, or
certify specific AI models, vendors, or platforms as safe or reliable.

Certification through this protocol verifies that an organization
has honest audit infrastructure. It does not verify that their
AI system is free of harmful outputs, biases, or failure modes.
Some certifications (e.g., `FRAGILE_VALID` or `TOPOLOGICALLY_ISOLATED`)
explicitly warn of structural weaknesses; they do not imply
system safety or reliability.

Any representation that Sovereign Certification implies AI system
safety — beyond the specific infrastructure assessed — is
a misrepresentation of certification scope.

---

## 8. ALIGNMENT WITH INTERNATIONAL STANDARDS

This protocol's ethical framework is aligned with:

- **OECD Principles on Artificial Intelligence (2019)** — transparency,
  accountability, and human oversight
- **UNESCO Recommendation on the Ethics of AI (2021)** — human dignity,
  privacy, and the right to remedy
- **UN Guiding Principles on Business and Human Rights** — corporate
  responsibility to respect human rights in AI deployment
- **EU AI Act principles** — risk-based approach, transparency,
  human oversight of high-risk systems
- **IEEE Ethically Aligned Design** — prioritizing human well-being
  in the design of autonomous and intelligent systems

Alignment is declared, not certified. This protocol does not
hold regulatory approval under any of the above instruments.
Alignment means the design choices made here are consistent
with the principles those instruments establish.

---

## 9. JURISDICTION AND CONFLICTING LAWS

This ethics statement applies to the author and to the use of the
Sovereign Trace Protocol in jurisdictions where it is consistent
with local law. Users in jurisdictions with laws that conflict
with any provision of this statement should consult legal counsel
before using the protocol. The author does not require users to
violate the laws of their country.

---

## 10. REPORTING VIOLATIONS

Ethics concerns or violations of this statement may be reported
by **any party** (users, third parties, whistleblowers) via a
GitHub issue with label `ethics-concern` in this repository.
The reporter should provide evidence. The author will review
and, if confirmed, take appropriate action (e.g., public notice,
license termination, Trust Registry annotation).

All reports are reviewed by Sheldon K. Salmon personally.
Reports will be acknowledged within 14 days.

---

## 11. COMMITMENT TO PERIODIC REVIEW

This ethics statement shall be reviewed **annually** (or upon
any major change in AI law, ethics norms, or significant
updates to the protocol) and updated as necessary.
Version history will be preserved in git. Changes will be
documented in the changelog.

---

*AI-ETHICS-STATEMENT.md — v1.1 (June 2026)*  
*Sovereign Trace Protocol | Sheldon K. Salmon — AI Reliability & ADI/AGI Architect*  
*This statement is part of the immutable epistemic record.*
