# 🛡️ TokenShield & Context++

> **Universal AI Coding Token Economizer, Model Fatigue Shield & Context Carry-Over Suite**  
> *Cut your Cursor, Claude Code, Windsurf & Aider token bills by 70–90% while preventing AI hallucination across 4,000+ file codebases.*

---

## 📦 What is TokenShield & Context++?

Modern AI coding agents (Cursor, Claude Code, Windsurf, Aider) suffer from two massive problems:
1. **Model Fatigue & Context Amnesia:** When codebases grow, agents blindly reload 50KB–200KB source files into context on every turn. They lose track of earlier architectural decisions and start hallucinating broken imports.
2. **Exploding Cloud Token Bills:** Reading whole files just to inspect a 2-line function signature costs $0.10–$0.50 per query, quickly generating hundreds of dollars in monthly API bills.

**TokenShield solves this at the root by using the hardware you already paid for:**
- **Hybrid Dense + Sparse RAG (Light RAG):** Fuses sub-3ms in-memory **SQLite FTS5 BM25** for exact symbol lookups with **Dense Semantic Vector Estimation** (local BGE-M3 or Qwen embeddings in the execution path via LM Studio/Ollama) and a zero-dependency **In-RAM Redis TCP cache (< 0.1ms)**. When agents ask for callers, types, or conceptual logic, TokenShield returns exact 5-line snippets in under 15ms without sending 50KB files to cloud LLMs.
- **Hardware-First Interception:** Your workstation has 32GB–64GB+ RAM, fast multi-core CPUs, and an idle GPU. TokenShield acts as an invisible context firewall between your editor (Cursor, Windsurf, VS Code) and cloud APIs (Claude, OpenAI) by routing code discovery and AST indexing through local hardware.
- **Autonomic Local Model Manager:** Probes local AI engines (Ollama on port 11434, LM Studio on port 1234). Runs lightweight coder models like `qwen2.5-coder:1.5b` completely offline at **$0 cloud cost** to catch syntax errors, missing brackets, and typos before uploading.
- **Low-RAM Mode & Mixed Pipeline:** Have a lightweight laptop with 8–16GB RAM? Turn off the local LLM code checker with 1 command (`npx tokenshield low-ram on`) while keeping ultra-fast In-RAM AST RAG active! Automatically upgrades to dense semantic search and local GPU auditing when extra hardware is detected.
- **Chat Context Carry-Over:** Snapshot active tasks, touched files, and architectural decisions into a stack (`chat push` / `chat pop`), or export portable bundles (`chat export` / `chat import`) to pick up across conversations and machines without context loss.
- **Free Evaluation Mode (Try Before You Buy):** TokenShield operates out of the box in free evaluation mode right inside your editor so you can verify AST queries and real-time token savings before unlocking perpetual lifetime updates.
- **Where Telemetry is Shown:** Real-time token counts and dollar savings in your CLI, bottom VS Code status bar widget (`🛡️ TokenShield: 167k saved ($3.35)`), local JSON vault, and verified web pass.

---

## 🔒 Zero-PII Privacy & Local-Only Guarantee

**TokenShield runs 100% locally on your machine.**

- **Zero Source Code Leaks:** Your proprietary source code, AST call-graphs, SQLite RAM databases, prompt text, and git diffs **never leave your local hardware**.
- **No Remote Telemetry Tracking:** Detailed tool invocation traces, local logs, and file paths are stored strictly on your local disk in `.agents/telemetry/`.
- **Anonymous Global Community Counter:** The only outbound network ping is an anonymous, lightweight counter sent to `praveenojha.com` to power the live public community token savings ticker:
  ```json
  { "tokens_saved": 48200, "ide": "vscode" }
  ```
  Strictly an aggregate numeric token count and the IDE client name are transmitted. No user IDs, no IP logging, and no project metadata.

---

## 💡 The Origin Story: Why We Built TokenShield

TokenShield was not created in a vacuum or as a theoretical demo. It was forged in production battle while building **PortSync** alongside modernized cross-platform applications like **Animal Vision** and **Thermal Camera**.

As our unified architecture grew past **4,400+ files and 4 interconnected workspaces**, we hit a brutal wall that every serious developer using AI coding agents eventually runs into:
1. **The Model Could Not Comprehend the Entire Codebase:** Modern frontier models (Claude 3.5 Sonnet, GPT-4o, Cursor Agent) cannot hold 4,000 files in active memory without severe attention dilution. Even with 200k token windows, "context rot" caused the AI to forget core architectural patterns, break existing imports, and hallucinate outdated conventions.
2. **Astronomical Token Bills:** Asking simple questions like *"Where is this route handler invoked?"* triggered massive context dumps of 50KB–200KB per turn, racking up hundreds of dollars in API bills each week.
3. **Model Fatigue & Context Amnesia:** Long coding sessions degraded rapidly. After 15 turns, the agent would lose track of what it had edited in turn 3, rewriting working code and causing endless loop errors.

**We had to build TokenShield to solve our own daily crisis:**
By moving AST call-graph indexing into sub-15ms local RAM (SQLite BM25), pre-flighting syntax on local GPUs/CPUs at $0 cost, and creating a cryptographic context push/pop carry-over vault, our AI agents went from fatigued and amnesiac to **laser-focused and architecturally disciplined**.

In our first few days alone, TokenShield saved **167,400+ cloud tokens**, cut API costs by 84%, and allowed us to ship PortSync, Animal Vision, and Thermal Camera without hitting token caps or model fatigue. We are now sharing this exact internal battery with the global developer community.

---

## 🎨 Standalone Assets & Icons

TokenShield uses standalone, cropped individual PNG icons:

| Asset | Preview | Purpose |
|---|---|---|
| **TokenShield Emblem** | `assets/icon.png` | Main product shield emblem with neon emerald core |
| **AST Tree Graph** | `assets/tokenshield_ast.png` | In-RAM Call-Graph and SQLite BM25 indexing engine |
| **Lightning Token Meter** | `assets/tokenshield_meter.png` | Real-time token economizer and dollar cost tracker |
| **Terminal Pulse** | `assets/tokenshield_terminal.png` | Context carry-over and CLI command prompt |
| **Accelerated Chip** | `assets/tokenshield_chip.png` | Local GPU/CPU offline model pre-flight validator |

---

## ⚙️ System Dependencies & Autonomous Installation

TokenShield is engineered for **zero manual configuration**:

| Dependency | Purpose | How TokenShield Handles It |
|---|---|---|
| **Python 3** | Core AST parser & SQLite BM25 | **Auto-Detected:** Uses your existing `python3` or `python` in PATH. Never duplicates if already present. |
| **Node.js** | Developer CLI & MCP server | **Auto-Detected:** Uses your existing `node` in PATH. |
| **Ollama** | Offline GPU/CPU code audits ($0) | **Auto-Installed:** Run `npx tokenshield install-ollama` (or curl 1-liner) if not found. |
| **Docker & Redis** | Sub-0.99ms In-RAM RAM cache | **Auto-Provisioned:** Starts Docker container `tokenshield-redis` or native `redis-server`. If absent, **falls back seamlessly to built-in SQLite BM25 in-RAM mode (<2ms)** with zero external dependencies required! |

---

## 💻 Universal Multi-IDE Installation Guide

TokenShield operates across all major AI coding IDEs, terminals, and agents:

| IDE / Environment | Installation Method | Configuration Target |
|---|---|---|
| **VS Code** | Install from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=praveenojha.tokenshield-contextplus) or `code --install-extension tokenshield.vsix` | Extension Sidebar & Status Bar |
| **Cursor** | Search `TokenShield` in Extensions (Open-VSX) or `cursor --install-extension tokenshield.vsix` | `.cursor/mcp.json` & `.cursorrules` |
| **Windsurf (Codeium)** | Search `TokenShield` in Extensions (Open-VSX) or `windsurf --install-extension tokenshield.vsix` | `.codeium/windsurf/mcp_config.json` & `.windsurfrules` |
| **Claude Desktop** | Run `npx tokenshield setup-mcp` | `claude_desktop_config.json` |
| **Claude Code (CLI)** | Run `npx tokenshield setup-mcp` | `~/.claude.json` & `CLAUDE.md` |
| **Gemini / Antigravity Agent** | Run `npx tokenshield setup-mcp` | `.agents/mcp_config.json` & `.agents/rules/tokenshield.md` |
| **JetBrains (IntelliJ, WebStorm, PyCharm)** | Configure Model Context Protocol (MCP) using `npx tokenshield mcp` | JetBrains Stdio MCP Bridge |
| **Terminal / Neovim / Zed / Aider** | Run `npx tokenshield self-install` or launch Cockpit: `npx tokenshield tui` | Interactive Terminal UI (TUI) |

### ⚡ 1-Command Universal Auto-Registration
Run this single command in any workspace to register TokenShield across **all detected IDEs**:
```bash
npx tokenshield setup-mcp
```
This automatically scans your system and configures VS Code, Cursor, Windsurf, Claude Desktop, Claude Code, and Gemini/Antigravity in < 50ms!

---

## 🚀 Quick Start (1 Minute)

### 1. Install & Arm Your Project
```bash
# In your project repository:
npx tokenshield-contextplus init
# or if installed globally:
tokenshield init
```
This automatically indexes your code into `.agents/.rag_memory.db`, configures `.agents/mcp_config.json`, and injects context-saving rules into `.cursorrules`.

### 2. Verify Hardware & Model Status
```bash
npx tokenshield status
npx tokenshield models
```

### 3. Search Symbols with Zero Token Bloat (<15ms)
```bash
npx tokenshield ref getStoreOrder
```

### 4. Offline Pre-Flight Linting ($0.00 Cloud Cost)
```bash
npx tokenshield lint src/app/page.tsx
```

---

## 🎛️ Modular Component Controls (Low-RAM Optimization)

Don't have enough RAM or GPU VRAM for local LLMs? Or only need specific components? Customize your setup anytime:

```bash
# View active module states
npx tokenshield config

# 1-Click Low-RAM Mode (disables heavy local LLMs, saves 8-14 GB RAM):
npx tokenshield low-ram on

# Turn off specific modules:
npx tokenshield disable code_checker    # Disables local LLM; uses instant zero-RAM syntax linter
npx tokenshield disable ast_rag         # Disables In-RAM AST cache

# Turn modules back on:
npx tokenshield enable code_checker
npx tokenshield enable ast_rag
```

---

## 🔄 Chat Context Carry-Over (`push`, `pop`, `export`, `import`)

Never let your AI coding agent forget in-flight work:

```bash
# Push current active task & touched files into stash stack:
npx tokenshield chat push "before-auth-refactor"

# List all saved chat checkpoints:
npx tokenshield chat list

# Restore a previous context by #ID:
npx tokenshield chat load 1

# Pop stashed context back into active RAM:
npx tokenshield chat pop

# Export context into a portable JSON bundle for another machine:
npx tokenshield chat export my-feature-context.json

# Import context bundle on another machine:
npx tokenshield chat import my-feature-context.json
```

---

## 📊 Where Telemetry Is Displayed

1. **Terminal / CLI:**
   Run `npx tokenshield telemetry` to view instant latency, tool runs, tokens saved, and estimated USD prevented.
2. **VS Code / Cursor Status Bar:**
   Displays live bottom bar badge: `🛡️ TokenShield: 167k saved ($3.35)` with real-time updates.
3. **Local Encrypted Vault File:**
   Persisted on disk in `~/.tokenshield/vault.json` and `.agents/telemetry/tool_invocations.json` for offline auditability.
4. **Web Portal & Printable PDF:**
   Each purchase receives an official cryptographic PDF activation pass and instant web unlock link.

---

## 🔐 Entitlement Tiers: Free Trial vs. Pro Lifetime

| Feature | Free Community Trial | Personal Indie Pro ($29 Lifetime) | Team Agency Pro ($89 Lifetime) |
|---|---|---|---|
| **Token Savings Limit** | 100,000 tokens trial (100k) | **UNLIMITED Lifetime** | **UNLIMITED Lifetime** |
| **Chat Stashes (`push/pop`)** | Max 3 checkpoints | **UNLIMITED Stashes** | **UNLIMITED Stashes** |
| **Context Export/Import** | 2 transfers trial | **UNLIMITED Transfers** | **UNLIMITED Transfers** |
| **Local GPU Model Audits** | Capped at 25 runs | **UNLIMITED Offline Runs** | **UNLIMITED Offline Runs** |
| **In-RAM AST Text RAG** | Single repo | **All Local Repositories** | **Monorepos & Workspaces** |
| **License Seats & Devices** | 1 device (7-day trial) | **1 Seat (3 devices: Desktop/Laptop/Mac)** | **5 Seats (3 devices/seat = 15 total devices)** |

### How to Activate / Deactivate:
```bash
# Activate this machine
npx tokenshield activate <your-license-key>

# Deactivate to free up seat for another machine
npx tokenshield deactivate
```
> **Device Rotation (FIFO):** If you activate on a 4th device (or 6th for Agency), the oldest device activation is automatically rotated out. You can also run `npx tokenshield deactivate` to explicitly free up a seat.

Purchase official lifetime keys at: [https://praveenojha.com/store/tokenshield](https://praveenojha.com/store/tokenshield)

---

## 📋 Complete CLI Command Reference

| Command | Description |
|---|---|
| `npx tokenshield init` | Arms current workspace with In-RAM AST RAG & MCP server |
| `npx tokenshield status` | Displays active model, quota, tokens saved & cost savings |
| `npx tokenshield ref <sym>` | Sub-15ms symbol reference & signature lookup from RAM |
| `npx tokenshield lint <file>` | Offline local pre-flight syntax & runtime check ($0) |
| `npx tokenshield config` | Displays and manages modular component toggles |
| `npx tokenshield low-ram [on\|off]` | 1-click low-RAM mode (disables heavy local LLM models) |
| `npx tokenshield disable <mod>` | Turn off component (`code_checker`, `ast_rag`, etc.) |
| `npx tokenshield enable <mod>` | Turn on component |
| `npx tokenshield chat list` | List all saved chat contexts & active tasks |
| `npx tokenshield chat save [name]` | Save current chat context snapshot |
| `npx tokenshield chat load <id>` | Load historical chat context by #ID or name |
| `npx tokenshield chat push [tag]` | Push active context into stash stack |
| `npx tokenshield chat pop` | Pop stashed context back into active RAM |
| `npx tokenshield chat export [f]` | Export portable context JSON bundle |
| `npx tokenshield chat import <f>` | Import context bundle into active session |
| `npx tokenshield models` | Audit local hardware (probes Ollama & LM Studio) |
| `npx tokenshield install-ollama` | Auto-installs Ollama local AI runner |
| `npx tokenshield pull [model]` | Pulls offline coder model (e.g. `qwen2.5-coder:1.5b`) |
| `npx tokenshield diff` | Surgical unified diff extractor (84% token reduction) |
| `npx tokenshield telemetry` | Live session cost & token savings report |
| `npx tokenshield activate <key>` | Unlocks unlimited Lifetime Pro license |
| `npx tokenshield deactivate` | Frees up active seat for another machine |

---

© 2026 Praveen Ojha. All rights reserved.
Support: [support@praveenojha.com](mailto:support@praveenojha.com)
