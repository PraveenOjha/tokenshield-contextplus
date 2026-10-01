#!/usr/bin/env python3
"""
TokenShield & Context++ — Modular Configuration Manager
========================================================
Allows developers to enable/disable individual components based on their
hardware constraints (RAM, CPU/GPU) or workflow preferences.
"""

import os
import sys
import json

CONFIG_DIR = os.path.expanduser("~/.tokenshield")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "modules": {
        "ast_rag": True,            # In-RAM AST Text RAG engine
        "code_checker": True,       # Local LLM offline code checker (turn off if low RAM)
        "native_linter": True,      # Fast zero-RAM deterministic bracket & syntax parser
        "diff_economizer": True,    # Surgical lean diff extractor
        "session_compactor": True,  # Context compactor & memory compressor
        "audio_compressor": True,   # Audio Context Compressor & Token Guard (40-75% audio token savings)
        "telemetry": True           # Telemetry and token savings tracker
    },
    "low_ram_mode": False,          # Master switch for low-RAM machines (disables LLM models)
    "preferred_backend": "auto",    # "auto" | "lm_studio" | "ollama" | "native_ast"
    "active_model": "qwen2.5-coder:1.5b" # default local model for offline pre-flight
}

def get_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                cfg = DEFAULT_CONFIG.copy()
                cfg["modules"] = {**DEFAULT_CONFIG["modules"], **data.get("modules", {})}
                cfg["low_ram_mode"] = data.get("low_ram_mode", False)
                cfg["preferred_backend"] = data.get("preferred_backend", "auto")
                cfg["active_model"] = data.get("active_model", DEFAULT_CONFIG["active_model"])
                return cfg
        except Exception:
            pass
    return DEFAULT_CONFIG.copy()

def save_config(cfg):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)

def set_module_status(module_name: str, enabled: bool):
    cfg = get_config()
    module_clean = module_name.lower().replace("-", "_")

    if module_clean in ["low_ram", "low_ram_mode", "lowram"]:
        cfg["low_ram_mode"] = enabled
        if enabled:
            cfg["modules"]["code_checker"] = False
            print("⚡ Low-RAM Mode: ON. Heavy local LLM model checker disabled (0 RAM/VRAM load).")
        else:
            print("⚡ Low-RAM Mode: OFF.")
    elif module_clean in cfg["modules"]:
        cfg["modules"][module_clean] = enabled
        state = "ENABLED (ON)" if enabled else "DISABLED (OFF)"
        print(f"✓ Module '{module_clean}': {state}")
    else:
        print(f"⚠️ Unknown module '{module_name}'. Available: {list(cfg['modules'].keys()) + ['low_ram']}")
        return False

    save_config(cfg)
    return True

def set_model(model_name: str):
    cfg = get_config()
    cfg["active_model"] = model_name.strip()
    save_config(cfg)
    print(f"✓ Active Local LLM Model set to: '{cfg['active_model']}'")
    return True

def print_status():
    cfg = get_config()
    print("\n" + "=" * 65)
    print("🛡️  TOKENSHIELD & CONTEXT++ — MODULAR CONFIGURATION")
    print("=" * 65)
    print(f"Low-RAM Mode: {'⚡ ACTIVE (Zero-Model Mode)' if cfg.get('low_ram_mode') else '○ Inactive'}")
    print(f"Active Model: {cfg.get('active_model', 'qwen2.5-coder:1.5b')}")
    print("\nComponent Modules:")
    for mod, state in cfg["modules"].items():
        icon = "✓ ON " if state else "✗ OFF"
        desc = ""
        if mod == "ast_rag":
            desc = "In-RAM AST Text RAG (<15ms symbol search)"
        elif mod == "code_checker":
            desc = "Local LLM/GPU code auditor (requires RAM/VRAM)"
        elif mod == "native_linter":
            desc = "Instant deterministic syntax check (<5ms, 0 RAM)"
        elif mod == "diff_economizer":
            desc = "Surgical lean diff generator (84% token reduction)"
        elif mod == "session_compactor":
            desc = "Context memory compactor & truncation defense"
        elif mod == "audio_compressor":
            desc = "Audio Context Compressor & Token Guard (VAD & transcript compactor)"
        elif mod == "telemetry":
            desc = "Token savings and dollar audit tracker"
        print(f"  [{icon}] {mod:<18} — {desc}")
    print("=" * 65)
    print("💡 Commands to customize your setup:")
    print("   • Toggle module:  npx tokenshield disable code_checker")
    print("   • Low-RAM Mode:   npx tokenshield low-ram on   (saves 8-14 GB RAM)")
    print("   • Switch Model:   npx tokenshield set-model qwen2.5-coder:7b")
    print("   • Enable module:  npx tokenshield enable ast_rag\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in ["status", "list", "show"]:
            print_status()
        elif cmd in ["enable", "on"] and len(sys.argv) > 2:
            set_module_status(sys.argv[2], True)
        elif cmd in ["disable", "off"] and len(sys.argv) > 2:
            set_module_status(sys.argv[2], False)
        elif cmd in ["low-ram", "lowram"]:
            state = True
            if len(sys.argv) > 2:
                state = sys.argv[2].lower() in ["on", "true", "1", "yes"]
            set_module_status("low_ram", state)
        elif cmd in ["model", "get-model"]:
            if len(sys.argv) > 2:
                set_model(sys.argv[2])
            else:
                cfg = get_config()
                print(cfg.get("active_model", "qwen2.5-coder:1.5b"))
        elif cmd in ["set-model", "select-model"] and len(sys.argv) > 2:
            set_model(sys.argv[2])
        elif cmd == "set" and len(sys.argv) > 3:
            state = sys.argv[3].lower() in ["on", "true", "1", "yes"]
            set_module_status(sys.argv[2], state)
        else:
            print_status()
    else:
        print_status()
