graph TD
    A[User Input] --> B[Sovereign Trace CLI]
    B --> C{Seal or Verify?}
    C -->|Seal| D[Compute SHA-256]
    D --> E[Add Triple-Time Stamp<br/>(Gregorian + Hebrew + Dreamspell)]
    E --> F[Sign with Ed25519 Private Key]
    F --> G[Save to Ledger<br/>(JSON + GitHub Action)]
    G --> H[Optional: Anchor to<br/>Bitcoin / Hedera / Ethereum]
    C -->|Verify| I[Check Signature<br/>+ Hash Match]
    I --> J[Report: VALID / TAMPERED / EXPIRED]
