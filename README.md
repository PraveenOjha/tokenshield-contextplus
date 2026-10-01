<div align="center">

# 🛡️ TokenShield & Context++

**Universal AI Coding Token Economizer, Model Fatigue Shield & Context Carry-Over Suite**  
*Cut your Cursor, Claude Code, Windsurf & Aider token bills by 70–90% while preventing AI hallucination across 4,000+ file codebases.*

[![npm version](https://img.shields.io/npm/v/tokenshield-contextplus.svg?color=emerald&style=flat-square)](https://www.npmjs.com/package/tokenshield-contextplus)
[![npm downloads](https://img.shields.io/npm/dm/tokenshield-contextplus.svg?color=blue&style=flat-square)](https://www.npmjs.com/package/tokenshield-contextplus)
[![VS Code](https://img.shields.io/badge/VS_Code_Marketplace-v1.0.1-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=praveenojha.tokenshield-contextplus)
[![Open VSX](https://img.shields.io/badge/Open_VSX-v1.0.1-purple?style=flat-square&logo=eclipseide&logoColor=white)](https://open-vsx.org/extension/praveenojha/tokenshield-contextplus)
[![Claude MCP](https://img.shields.io/badge/Claude_MCP-JSON--RPC_Ready-D97706?style=flat-square&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io)
[![License: Commercial](https://img.shields.io/badge/License-Commercial%20%2F%20Proprietary-gold?style=flat-square)](LICENSE.md)
[![Store](https://img.shields.io/badge/Official_Store-praveenojha.com%2Ftokenshield-10B981?style=flat-square)](https://praveenojha.com/tokenshield)

</div>

---

> [!IMPORTANT]
> ### 🔒 Proprietary & Commercial Software Notice
> **TokenShield & Context++** is commercial, closed-source proprietary software authored and maintained by **[Praveen Ojha](https://praveenojha.com)**.
> - **The core runtime engine, AST indexing algorithms, In-RAM interceptor binaries, and licensing services are private and proprietary.**
> - **This public repository (`tokenshield-contextplus`) is the official public documentation, community support hub, integration guide, and issue tracker.**
> - Verified distributions and CLI packages are officially published to **[npm (`tokenshield-contextplus`)](https://www.npmjs.com/package/tokenshield-contextplus)**, the **[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=praveenojha.tokenshield-contextplus)**, and the **[Open VSX Registry](https://open-vsx.org/extension/praveenojha/tokenshield-contextplus)**.
> - Free evaluation mode works out of the box. Perpetual lifetime license keys (Personal Indie Pro & Team Agency Edition) can be obtained via the **[Official TokenShield Portal](https://praveenojha.com/tokenshield)**.

---

## ⚡ What is TokenShield & Context++?

Modern AI coding agents (**Cursor**, **Claude Code**, **Windsurf**, **Aider**, **Copilot**) suffer from two severe structural bottlenecks:

1. **The Context Bloat Paradox & Model Fatigue:** When codebases grow, agents blindly reload 50KB–200KB source files on every turn. In large 4,000+ file projects, "context rot" causes frontier models to lose earlier architectural decisions, invent non-existent APIs, and hallucinate broken imports.
2. **Exploding Cloud Token Bills:** Reading whole source files just to inspect a 2-line function signature costs $0.05–$0.25 per turn, quickly burning through hundreds of dollars in monthly API quotas.

**TokenShield solves this at the hardware level by using the machine you already paid for:**

- **Sub-15ms In-RAM AST Call-Graph:** Fuses SQLite FTS5 BM25 indexing with an In-RAM Redis socket cache (< 0.1ms). When your agent asks for types, definitions, or call sites, TokenShield feeds it surgical 5-line snippets instead of 2,000-line files.
- **Hardware-First Interception:** Routes code navigation and AST discovery through your workstation's local RAM and multi-core CPU, acting as an intelligent firewall between your editor and cloud LLM APIs.
- **Offline Local GPU Pre-Flight Lint ($0.00 Cost):** Intercepts syntax validation, missing brackets, and type audits by dispatching to local quantized models (e.g., Qwen2.5-Coder on Ollama/LM Studio) in < 1s offline at zero cloud cost.
- **Surgical Diff Economizer:** Strips out bloated boilerplate diffs and outputs high-density surgical unified patches, saving 70% to 95% of context window space.
- **Chat Context Carry-Over:** Snapshot active tasks, touched files, and architectural decisions into a persistent vault (`chat push` / `chat pop`), or export portable bundles (`chat export` / `chat import`) across machines without losing project state.
- **Low-RAM Mode:** On lightweight laptops (8–16GB RAM), run in ultra-light zero-LLM mode (`npx tokenshield low-ram on`) while preserving full In-RAM AST indexing speed.

---

## 📦 Standalone Assets & Visuals

| Asset | Preview | Purpose |
|---|---|---|
| **TokenShield Emblem** | `assets/icon.png` | Official shield emblem with emerald power core |
| **AST Tree Graph** | `assets/tokenshield_ast.png` | In-RAM Call-Graph and SQLite BM25 indexing engine |
| **Lightning Token Meter** | `assets/tokenshield_meter.png` | Real-time token economizer and dollar cost tracker |
| **Terminal Pulse** | `assets/tokenshield_terminal.png` | Context carry-over and CLI command prompt |
| **Accelerated Chip** | `assets/tokenshield_chip.png` | Local GPU/CPU offline model pre-flight validator |

---

## 🚀 Quick Start (1 Minute)

### Option A: Use On-the-Fly via npx (Zero Global Installs)

```bash
# In your project root directory:
npx -y tokenshield-contextplus init
```

### Option B: Install Globally via npm

```bash
npm install -g tokenshield-contextplus

# Initialize your project
tokenshield init
```

### Option C: VS Code, Cursor & Windsurf Extension

1. Open **VS Code**, **Cursor**, or **Windsurf**.
2. Press `Ctrl+P` (or `Cmd+P`) and run:
   ```text
   ext install praveenojha.tokenshield-contextplus
   ```
   *Available on both the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=praveenojha.tokenshield-contextplus) and [Open VSX](https://open-vsx.org/extension/praveenojha/tokenshield-contextplus).*
3. The live telemetry status bar widget (`🛡️ TokenShield: 167k saved ($3.35)`) will appear automatically.

### Option D: Native Claude Desktop & Claude Code (MCP Server)

Add TokenShield to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tokenshield": {
      "command": "npx",
      "args": ["-y", "tokenshield-contextplus", "mcp"]
    }
  }
}
```

Now, whenever Claude needs symbol references or code discovery, it invokes `tokenshield_ref` via JSON-RPC in **0.1ms**, using **120 tokens** instead of dumping 15,000-token files into Sonnet!

---

## 🧠 Architectural Reality Check: Why In-RAM Interception Wins

| Feature / Mechanism | Naive Prompt Trimmers (e.g. TokenSculpt) | 🛡️ TokenShield & Context++ |
|---|---|---|
| **Core Architecture** | Strips comments into an 800-line markdown file | **In-RAM Redis socket cache (<0.1ms) + SQLite BM25 index (<15ms)** |
| **The Prompt Bloat Paradox** | ⚠️ Re-sends the large markdown file every turn, **costing MORE tokens** over 10 turns | ✅ Feeds only exact 5-line typed signatures directly into tool results |
| **Hardware Utilization** | 0% (runs plain regex scripts) | **100% (leverages multi-core CPU, RAM & optional local GPU/VRAM)** |
| **Syntax & Pre-Flight Audits** | None (wastes $0.05 on Claude 3.5 to fix a typo) | **Local Qwen2.5-Coder model via LM Studio/Ollama ($0.00 cost in <1s)** |
| **Cross-Session Memory** | None (context is lost when chat closes) | **Persistent Live Work Vault (`push`, `pop`, `export`, `import`)** |
| **Native Integrations** | CLI only | **VS Code, Cursor, Windsurf, Claude MCP Server, npm, and REST** |

---

## 🛠️ CLI Command Reference

| Command | Description |
|---|---|
| `npx tokenshield init` | Arms current workspace with In-RAM AST RAG, MCP config, and `.cursorrules` |
| `npx tokenshield status` | Displays active hardware model, current quota, and token/dollar savings |
| `npx tokenshield ref <symbol>` | Sub-15ms symbol reference and typed signature lookup from RAM |
| `npx tokenshield lint <file>` | Offline local pre-flight syntax and bracket check at $0.00 cost |
| `npx tokenshield diff` | Surgical unified diff extractor (70%–95% context reduction) |
| `npx tokenshield telemetry` | Live session cost, latency, and token savings report |
| `npx tokenshield config` | Displays and configures modular component toggles |
| `npx tokenshield low-ram on\|off` | 1-click low-RAM mode (disables heavy local LLM inference) |
| `npx tokenshield chat push [tag]` | Push active task context & touched files into stash vault |
| `npx tokenshield chat pop` | Pop stashed context back into active RAM |
| `npx tokenshield chat list` | List all saved chat checkpoints and tasks |
| `npx tokenshield chat load <id>` | Load historical chat context by ID |
| `npx tokenshield chat export <f>` | Export portable context JSON bundle for another machine |
| `npx tokenshield chat import <f>` | Import context bundle into active session |
| `npx tokenshield activate <key>` | Unlocks unlimited Lifetime Pro license |
| `npx tokenshield deactivate` | Frees up active seat for another machine |

---

## 🔐 Licensing & Commercial Entitlements

TokenShield operates out of the box in **Free Evaluation Mode** with full AST lookup and real-time telemetry so you can verify token savings in your actual codebase before purchasing.

To unlock unlimited token tracking, perpetual stashes, multi-device sync, and team seats:

| Tier | Seats & Devices | Quota & Features | Buy Once |
|---|---|---|---|
| **Free Community Evaluation** | 1 device (evaluation) | 50,000 tokens tracked, 3 stashes | **Free** |
| **Personal Indie Pro** | 1 seat (3 devices: Desktop/Laptop/Mac) | **UNLIMITED Lifetime**, All repos, Local GPU pre-flight | **$29 Lifetime** |
| **Team & Agency Edition** | 5 seats (15 total devices) | **UNLIMITED Lifetime**, Monorepos, Team context sharing | **$89 Lifetime** |

👉 **Claim Your Lifetime License & Instant Activation Pass:**  
**[https://praveenojha.com/tokenshield](https://praveenojha.com/tokenshield)**

---

## 🤝 Community, Issues & Support

- **Bug Reports & Issues:** Please file any bug reports, integration queries, or IDE compatibility issues using our [GitHub Issues](https://github.com/PraveenOjha/tokenshield-contextplus/issues).
- **Security Inquiries:** For private security reports, contact [support@praveenojha.com](mailto:support@praveenojha.com).
- **Official Portal:** [https://praveenojha.com/tokenshield](https://praveenojha.com/tokenshield)

---

<div align="center">

Copyright © 2026 **Praveen Ojha** & PortSync Technologies. All rights reserved.  
*TokenShield™ and Context++™ are trademarks of Praveen Ojha.*

</div>
