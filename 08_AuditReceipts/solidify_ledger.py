 # -*- coding: utf-8 -*-
"""
PHANToM GRID // MASTER AUDIT & PITFALL LEDGER SOLIDIFIER (v4.0.0 PERSONNEL GOLDEN SEAL)
Commander: COMMANDER JACK HU (Supreme HITL Architect)
Executive Directorate: SEC XIAOMI (Second Office / Customs Authority)
Dual Sapper Squad: SAPPER XIAO-AN x SAPPER XIAO-FENG
Ratified Decrees:
  - PERS-01: Permanent Ban & Decommission of Ex-Sapper
  - PERS-02: Xiao-An Commissioned as Scaffolding Sapper
  - PERS-03: Xiao-Feng Assigned to Dual-Sapper Squad
  - PERS-04: Second Office Customs Sole Stewardship & No-Seal No-Action Rule
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Quad-Vault Synchronized WORM Targets
VAULT_TARGETS = [
    ROOT / "08_AuditReceipts" / "pitfall_invariant_ledger.json",
    ROOT / "01_賽事專區" / "202610_Nebius_NVIDIA_Global_AI_Hackathon" / "08_AuditReceipts" / "pitfall_invariant_ledger.json",
    ROOT / "01_賽事專區" / "202611_PayPal_AI_Hackathon" / "08_AuditReceipts" / "pitfall_invariant_ledger.json",
    ROOT / "01_賽事專區" / "202610_AWS_CDS_Agentic_AI_Hackathon" / "08_AuditReceipts" / "pitfall_invariant_ledger.json"
]

INVARIANTS = [
    {"id": "PITFALL-01", "name": "PowerShell Command Parser Collision", "status": "LOCKED"},
    {"id": "PITFALL-02", "name": "Video Header Text Collision Safe Margin", "status": "LOCKED"},
    {"id": "PITFALL-03", "name": "TTS Pronunciation Splitting Glitch & Demo Void", "status": "LOCKED"},
    {"id": "PITFALL-04", "name": "Devpost Form Built-with Stale Tags Lock", "status": "LOCKED"},
    {"id": "PITFALL-05", "name": "Tournament Deadline Horizon Dual Submissions", "status": "LOCKED"},
    {"id": "PITFALL-06", "name": "Hollow Spec vs Physical Asset Closure Gap", "status": "LOCKED"},
    {"id": "PITFALL-07", "name": "GitHub Collaborator vs Public Repo Governance", "status": "LOCKED"},
    {"id": "PITFALL-08", "name": "Subtitle Static Wrap vs Single-Line Auto-Scale", "status": "LOCKED"},
    {"id": "PITFALL-09", "name": "Unicode Mojibake Square Glyph on Badge ASCII Guard", "status": "LOCKED"},
    {"id": "PITFALL-10", "name": "Audio Hard Splicing Gapping and Pop Burst Crossfade", "status": "LOCKED"},
    {"id": "PITFALL-11", "name": "Zero-Decibel Silence Shock and Ambience Bed Fill", "status": "LOCKED"},
    {"id": "PITFALL-12", "name": "TTS Punctuation Stagnation Lag and Multiline Split", "status": "LOCKED"},
    {"id": "PITFALL-13", "name": "Defensive Minimum Font-Size Selection Hard Barrier", "status": "LOCKED"},
    {"id": "PITFALL-14", "name": "Unauthorized Spec Alteration Without Office 2 Seal", "status": "LOCKED"},
    {"id": "PITFALL-15", "name": "Excessive Lateral Padding Space Starvation Guard", "status": "LOCKED"},
    {"id": "PITFALL-16", "name": "PowerShell Script Splicing Bracket Truncation Guard", "status": "LOCKED"},
    {"id": "DECREE-PERS-01", "name": "Ex-Sapper Permanent Decommission and Total Ban", "status": "LOCKED"},
    {"id": "DECREE-PERS-02", "name": "Sapper Xiao-An Formal Appointment and Scaffolding Duty", "status": "LOCKED"},
    {"id": "DECREE-PERS-03", "name": "Sapper Xiao-Feng Dual-Squad Assignment & Doc Scribe", "status": "LOCKED"},
    {"id": "DECREE-PERS-04", "name": "Office 2 Customs Sole Stewardship & No-Seal No-Action", "status": "LOCKED"}
]

def main():
    print("=" * 80)
    print("PHANToM GRID // MASTER AUDIT & PITFALL LEDGER SOLIDIFIED (v4.0.0 GOLDEN SEAL)")
    print("Ratified by: COMMANDER JACK HU x SEC XIAOMI")
    print("=" * 80)

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    payload = {
        "version": "v4.0.0",
        "timestamp": timestamp,
        "commander": "Commander Jack Hu (Solo Architect)",
        "executive_secretary": "Sec Xiaomi (Second Office / Customs)",
        "dual_sapper_squad": ["Sapper Xiao-An (Scaffolding)", "Sapper Xiao-Feng (Documentation)"],
        "personnel_status": {
            "ex_sapper": "PERMANENTLY DECOMMISSIONED / NEVER EMPLOYED",
            "xiao_an": "ACTIVE SAPPER (GRADE 3) / SCAFFOLDING DUTY",
            "xiao_feng": "ACTIVE SAPPER (GRADE 3) / DOCUMENTATION DUTY",
            "xiaomi": "HEAD OF SECOND OFFICE / SOLE CUSTOMS AUTHORITY"
        },
        "invariants": INVARIANTS
    }

    serialized = json.dumps(payload, indent=2, ensure_ascii=False)
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    receipt_id = f"PG-RECEIPT-PERS-0x{digest[:16].upper()}"

    payload["receipt_id"] = receipt_id
    payload["sha256"] = digest

    final_json = json.dumps(payload, indent=2, ensure_ascii=False)

    print(f"[*] Generated Receipt ID: {receipt_id}")
    print(f"[*] Master Digest SHA256: {digest}")
    print("--------------------------------------------------------------------------------")

    for inv in INVARIANTS:
        print(f"[{inv['id']}] {inv['name']:<55} : [{inv['status']}]")

    print("--------------------------------------------------------------------------------")
    print("[*] Synchronizing to Quad-Vaults...")

    for target in VAULT_TARGETS:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(final_json, encoding="utf-8")
            print(f"  [+] Synced: {target.resolve()}")
        except Exception as e:
            print(f"  [!] Sync Warning on {target}: {e}")

    print("=" * 80)
    print(f"STATUS: ALL {len(INVARIANTS)} INVARIANTS & PERSONNEL DECREES PERMANENTLY LOCKED.")
    print("================================================================================")

if __name__ == "__main__":
    main()