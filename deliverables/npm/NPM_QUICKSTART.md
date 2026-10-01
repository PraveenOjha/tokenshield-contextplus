# TokenShield ContextPlus — npm CLI & MCP Deliverables

## Package Info
- **Package Name:** `tokenshield-contextplus`
- **Binary Executable:** `tokenshield` / `cli.js`
- **Global Install Command:** `npm install -g tokenshield-contextplus`
- **Local Link Command:** `npm link` (from `ai-tools/tokenshield/`)

---

## 🚀 Quickstart Commands

```bash
# 1. Check armed status & hardware backend
tokenshield status

# 2. In-RAM AST Call-Graph (<15ms, saves 80% context tokens)
tokenshield ref <FunctionNameOrClass>

# 3. Offline Local GPU Pre-Flight Lint (0 cloud tokens)
tokenshield lint <filepath>

# 4. Surgical Lean Diff Economizer (70-90% token reduction)
tokenshield diff

# 5. Live Telemetry & Measured Token Conservation
tokenshield telemetry

# 6. List and Switch Local Models (LM Studio / Ollama)
tokenshield model
tokenshield set-model "qwen2.5-coder-7b-instruct"

# 7. Start Standard MCP Server (Claude Desktop / Claude Code / Windsurf)
tokenshield mcp
```

---

## Zero-Dependency Engine Architecture
- **Pure Standard Library:** The underlying Python engines require **zero pip packages**.
- **Cross-Platform:** Works on Linux, macOS, and Windows.
- **Auto-Fallback:** Seamlessly operates in BM25 SQLite In-RAM mode if LM Studio is not active.
