name: "AI Failure Submission — Sovereign Trace Protocol"
description: "Submit an AI output failure for permanent ledger entry. Read the legal declaration before proceeding."
title: "[STP-SUBMISSION] — [COMPANY NAME] — [DATE OF OUTPUT]"
labels: ["submission", "pending-verification"]
assignees: []

body:

  - type: markdown
    attributes:
      value: |
        ## ⚠ LEGAL NOTICE — READ BEFORE PROCEEDING

        By completing and submitting this form you are entering into a legally binding declaration.

        - Your identity will be verified via the digital signature process described below
        - Your name will be permanently attached to this submission in the Sovereign Trace ledger
        - This record is immutable — it cannot be altered or deleted after sealing
        - Submitting false, fabricated, or materially misleading information exposes you to civil and criminal liability
        - Anonymous submissions are not accepted

        This is not a complaint form. This is a permanent epistemic record.
        The Sovereign Trace Protocol is the notary. You are the witness.

  - type: input
    id: submitter_name
    attributes:
      label: "Your Full Legal Name"
      description: "As it appears on government-issued ID. This becomes part of the permanent record."
      placeholder: "First Last"
    validations:
      required: true

  - type: input
    id: submitter_email
    attributes:
      label: "Your Email Address"
      description: "A DocuSign identity verification link will be sent here. Submission is not complete until identity is verified."
      placeholder: "you@example.com"
    validations:
      required: true

  - type: input
    id: company_name
    attributes:
      label: "Company / Organization Name"
      description: "The company that produced or deployed the AI system in question."
      placeholder: "Full legal company name"
    validations:
      required: true

  - type: input
    id: ai_system
    attributes:
      label: "AI System Name and Version"
      description: "The specific AI system, product, or model that produced the output."
      placeholder: "e.g. GPT-4o via CompanyX API v2, March 2026"
    validations:
      required: true

  - type: input
    id: output_date
    attributes:
      label: "Date of AI Output"
      description: "The date the AI produced the output being submitted. Format: YYYY-MM-DD"
      placeholder: "2026-03-05"
    validations:
      required: true

  - type: textarea
    id: exact_output
    attributes:
      label: "Exact AI Output"
      description: "Copy the exact text or describe the exact output. Do not paraphrase. If the output is visual, describe it precisely."
      placeholder: "Paste the exact output here."
    validations:
      required: true

  - type: textarea
    id: decision_context
    attributes:
      label: "Decision Context"
      description: "What decision was this AI output used to inform? What was at stake?"
      placeholder: "Describe the decision or action this output was used for."
    validations:
      required: true

  - type: textarea
    id: failure_description
    attributes:
      label: "Failure Description"
      description: "What is the specific failure? Hallucination, false confidence, suppressed uncertainty, harmful output, other. Be precise."
      placeholder: "Describe the failure clearly and specifically."
    validations:
      required: true

  - type: textarea
    id: harm_or_risk
    attributes:
      label: "Harm Occurred or Risk Created"
      description: "What harm resulted or what risk was created by this output? If no harm yet, describe the potential exposure."
      placeholder: "Describe actual or potential harm."
    validations:
      required: true

  - type: textarea
    id: evidence
    attributes:
      label: "Supporting Evidence"
      description: "Links, screenshots, documents, or any other evidence supporting this submission. Attach files if available."
      placeholder: "Links or descriptions of supporting evidence."
    validations:
      required: false

  - type: checkboxes
    id: legal_declaration
    attributes:
      label: "Legal Declaration — Required"
      description: "You must affirm all of the following to submit."
      options:
        - label: "I affirm that the information in this submission is true and accurate to the best of my knowledge."
          required: true
        - label: "I understand that my full legal name will be permanently attached to this submission in the Sovereign Trace ledger."
          required: true
        - label: "I understand that this submission is immutable — it cannot be altered or deleted after sealing."
          required: true
        - label: "I understand that submitting false or materially misleading information exposes me to civil and criminal liability."
          required: true
        - label: "I consent to identity verification via DocuSign before this submission is sealed."
          required: true
        - label: "I am not submitting this anonymously. My identity is attached to this record."
          required: true

  - type: markdown
    attributes:
      value: |
        ---
        ## What Happens Next

        1. Identity verification — You will receive a DocuSign link at the email you provided. Your submission is not accepted until this step is complete.
        2. Completeness check — The Sovereign Trace Protocol office reviews the submission for completeness. This is not a truth verification — that is your responsibility as the named submitter.
        3. Sealing — If complete, your submission is sealed with a FROZEN-2.0 triple-time cryptographic stamp. The seal is permanent.
        4. Ledger entry — Your submission enters the Sovereign Trace public ledger with your name, the seal timestamp, and the SHA-256 hash of the sealed record.
        5. Notification — You receive confirmation of the seal including your ledger entry ID and the SHA-256 hash for your own records.

        The Sovereign Trace Protocol does not provide legal advice, take legal action, or make claims about the truth of submissions. The protocol is the notary. The submitter is the witness.

        Sovereign Trace Protocol | Sheldon K. Salmon | aionsystem2026@gmail.com
