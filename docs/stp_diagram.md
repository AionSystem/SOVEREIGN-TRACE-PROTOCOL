## STP Protocol Flow

```mermaid
flowchart TD
    A["User Input (text, file, or data)"] --> B{Choose Operation}
    
    B -->|Seal| C["Compute SHA-256 hash"]
    C --> D["Add Triple Timestamp\n(Gregorian + Hebrew + Dreamspell)"]
    D --> E["Sign with Ed25519 Private Key"]
    E --> F["Save to Ledger (JSON file)"]
    F --> G["Optional: Anchor to\nBitcoin / Hedera / Ethereum"]
    G --> H["Return Seal JSON + Timestamp + Signature"]
    
    B -->|Verify| I["Load Seal JSON"]
    I --> J["Verify Signature using Public Key"]
    J --> K["Recompute Hash of Original Data"]
    K --> L{Hash Match?}
    L -->|Yes| M["✅ VALID – Data intact"]
    L -->|No| N["❌ TAMPERED – Data changed"]
    
    H --> O["💾 Download Seal"]
    M --> O
    N --> O
