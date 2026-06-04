#!/usr/bin/env python3
"""
STP Multi‑Blockchain Anchor – Post Merkle root of new STP seals to Bitcoin, Hedera, Ethereum, and optionally Stellar.
Runs daily via GitHub Actions. State file tracks last processed issue.
"""

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from typing import List, Dict, Any

# ----------------------------------------------------------------------
# Configuration – read from environment
# ----------------------------------------------------------------------
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY")  # "AionSystem/SOVEREIGN-TRACE-PROTOCOL"
STATE_FILE = "stp_anchor_state.json"

# Blockchain flags (enable/disable)
ENABLE_BITCOIN = os.environ.get("ENABLE_BITCOIN", "true").lower() == "true"
ENABLE_HEDERA = os.environ.get("ENABLE_HEDERA", "true").lower() == "true"
ENABLE_ETHEREUM = os.environ.get("ENABLE_ETHEREUM", "true").lower() == "true"
ENABLE_STELLAR = os.environ.get("ENABLE_STELLAR", "false").lower() == "true"

# Bitcoin
BTC_RPC_URL = os.environ.get("BTC_RPC_URL")
BTC_RPC_USER = os.environ.get("BTC_RPC_USER")
BTC_RPC_PASS = os.environ.get("BTC_RPC_PASS")

# Hedera
HEDERA_ACCOUNT_ID = os.environ.get("HEDERA_ACCOUNT_ID")
HEDERA_PRIVATE_KEY = os.environ.get("HEDERA_PRIVATE_KEY")
HEDERA_TOPIC_ID = os.environ.get("HEDERA_TOPIC_ID", "0.0.123456")  # replace with your topic

# Ethereum
ETH_RPC_URL = os.environ.get("ETH_RPC_URL")          # e.g., Infura endpoint
ETH_PRIVATE_KEY = os.environ.get("ETH_PRIVATE_KEY")
ETH_CONTRACT_ADDRESS = os.environ.get("ETH_CONTRACT_ADDRESS")  # optional: custom contract to emit event

# Stellar (optional)
STELLAR_SECRET_KEY = os.environ.get("STELLAR_SECRET_KEY")
STELLAR_DISTRIBUTION_ACCOUNT = os.environ.get("STELLAR_DISTRIBUTION_ACCOUNT")


# ----------------------------------------------------------------------
# GitHub Issue Fetching (using API)
# ----------------------------------------------------------------------
def get_stp_issues_since(last_issue_id: int) -> List[Dict[str, Any]]:
    """Fetch all closed issues with label 'sealed' since last run."""
    import requests
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}
    params = {"state": "closed", "labels": "sealed", "per_page": 100, "sort": "created", "direction": "asc"}
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    issues = []
    page = 1
    while True:
        params["page"] = page
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data:
            break
        for issue in data:
            if issue.get("number", 0) > last_issue_id:
                # Build a unique seal hash from issue metadata.
                # In production, you would extract the actual STP seal hash from the issue body/comment.
                # For now, we use a deterministic hash of issue URL + creation time + title.
                seal_data = f"{issue['html_url']}\n{issue['created_at']}\n{issue['title']}"
                seal_hash = hashlib.sha256(seal_data.encode()).hexdigest()
                issues.append({"number": issue["number"], "hash": seal_hash})
        page += 1
    return issues


def build_merkle_root(hashes: List[str]) -> str:
    """Build Merkle root from list of SHA-256 hex strings."""
    if not hashes:
        return hashlib.sha256(b"STP_EMPTY_BATCH").hexdigest()
    current = [bytes.fromhex(h) for h in hashes]
    while len(current) > 1:
        if len(current) % 2 == 1:
            current.append(current[-1])
        next_level = []
        for i in range(0, len(current), 2):
            combined = current[i] + current[i+1]
            next_level.append(hashlib.sha256(combined).digest())
        current = next_level
    return current[0].hex()


# ----------------------------------------------------------------------
# Blockchain Posting (multi‑chain)
# ----------------------------------------------------------------------
def post_to_bitcoin(merkle_root: str) -> str:
    """Post OP_RETURN with merkle root to Bitcoin (requires RPC)."""
    import requests
    # Simplified: create raw transaction with OP_RETURN output.
    # For production, use `createrawtransaction` with OP_RETURN, then fund, sign, send.
    # This stub returns a dummy txid.
    print(f"Bitcoin anchor: would post merkle root {merkle_root}")
    return "dummy_btc_txid_placeholder"


def post_to_hedera(merkle_root: str) -> str:
    """Post merkle root to Hedera Consensus Service."""
    try:
        from hedera import Client, TopicMessageSubmitTransaction, PrivateKey, AccountId
    except ImportError:
        print("Hedera SDK not installed. Install with: pip install hedera-sdk-py")
        return "hedera_sdk_missing"
    client = Client.forTestnet()  # Change to forMainnet() for production
    client.setOperator(AccountId.fromString(HEDERA_ACCOUNT_ID), PrivateKey.fromString(HEDERA_PRIVATE_KEY))
    topic_id = HEDERA_TOPIC_ID
    transaction = TopicMessageSubmitTransaction(topic_id, merkle_root.encode())
    receipt = transaction.execute(client).getReceipt(client)
    return str(receipt.transactionId)


def post_to_ethereum(merkle_root: str) -> str:
    """Post merkle root to Ethereum (emit event from a contract)."""
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
    if not w3.is_connected():
        return "eth_not_connected"
    account = w3.eth.account.from_key(ETH_PRIVATE_KEY)
    # If we have a contract with an event `Anchor(bytes32 root)`, call it.
    # Otherwise, we can send a transaction with a data payload (simple fallback).
    # For simplicity, we create a raw transaction with merkle root in input data.
    # Real implementation would interact with a deployed STP anchor contract.
    nonce = w3.eth.get_transaction_count(account.address)
    tx = {
        'nonce': nonce,
        'to': ETH_CONTRACT_ADDRESS if ETH_CONTRACT_ADDRESS else account.address,
        'value': 0,
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
        'data': '0x' + merkle_root,
    }
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return tx_hash.hex()


def post_to_stellar(merkle_root: str) -> str:
    """Post merkle root to Stellar (optional)."""
    try:
        from stellar_sdk import Server, Keypair, TransactionBuilder, Network
    except ImportError:
        return "stellar_sdk_missing"
    server = Server("https://horizon-testnet.stellar.org")
    keypair = Keypair.from_secret(STELLAR_SECRET_KEY)
    account = server.load_account(keypair.public_key)
    # Create a memo with the merkle root (truncated to 28 chars for text memo, or use hash memo)
    # We'll use a text memo with the first 28 chars of the root.
    memo_text = merkle_root[:28]
    transaction = TransactionBuilder(
        source_account=account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100
    ).append_payment_op(
        destination=STELLAR_DISTRIBUTION_ACCOUNT,
        amount="0.00001",
        asset_code="XLM"
    ).add_text_memo(memo_text).build()
    transaction.sign(keypair)
    response = server.submit_transaction(transaction)
    return response["id"]


# ----------------------------------------------------------------------
# State Management
# ----------------------------------------------------------------------
def load_state() -> int:
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE, "r") as f:
        return json.load(f).get("last_issue_id", 0)


def save_state(last_issue_id: int):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_issue_id": last_issue_id, "last_anchor_time": datetime.now(timezone.utc).isoformat()}, f)


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    if not GITHUB_TOKEN:
        print("Missing GITHUB_TOKEN. Set environment variable.")
        sys.exit(1)

    last_id = load_state()
    new_issues = get_stp_issues_since(last_id)
    if not new_issues:
        print("No new STP seals since last anchor.")
        return

    hashes = [issue["hash"] for issue in new_issues]
    merkle_root = build_merkle_root(hashes)
    print(f"Merkle root for {len(new_issues)} seals: {merkle_root}")

    results = {}
    if ENABLE_BITCOIN and BTC_RPC_URL:
        results["bitcoin"] = post_to_bitcoin(merkle_root)
    if ENABLE_HEDERA and HEDERA_ACCOUNT_ID:
        results["hedera"] = post_to_hedera(merkle_root)
    if ENABLE_ETHEREUM and ETH_RPC_URL:
        results["ethereum"] = post_to_ethereum(merkle_root)
    if ENABLE_STELLAR and STELLAR_SECRET_KEY:
        results["stellar"] = post_to_stellar(merkle_root)

    print(f"Anchor results: {results}")

    # Optionally create a new issue to record the anchor
    # (can be implemented later)

    save_state(new_issues[-1]["number"])


if __name__ == "__main__":
    main()
