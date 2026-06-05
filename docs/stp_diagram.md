## STP Protocol Flow

```mermaid
flowchart TD
    A[User Input<br/>(text, file, or data)] --> B{Choose Operation}
    
    B -->|Seal| C[Compute SHA-256 hash]
    C --> D[Add Triple Timestamp<br/>Gregorian + Hebrew + Dreamspell]
    D --> E[Sign with Ed25519<br/>Private Key]
    E --> F[Save to Ledger<br/>(JSON file)]
    F --> G[Optional: Anchor to<br/>Bitcoin / Hedera / Ethereum]
    G --> H[Return Seal JSON<br/>+ Timestamp + Signature]
    
    B -->|Verify| I[Load Seal JSON]
    I --> J[Verify Signature<br/>using Public Key]
    J --> K[Recompute Hash<br/>of Original Data]
    K --> L{Hash Match?}
    L -->|Yes| M[✅ VALID – Data intact]
    L -->|No| N[❌ TAMPERED – Data changed]
    
    H --> O[💾 Download Seal]
    M --> O
    N --> O
