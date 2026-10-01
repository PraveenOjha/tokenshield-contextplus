# 🤖 Claude Desktop & Claude Code MCP Integration Deliverables

> **Official Model Context Protocol (MCP) Integration for TokenShield & Context++**  
> *Connect Anthropic Claude Desktop and Claude Code CLI to your local In-RAM AST RAG and hardware interceptor.*

---

## ⚡ What is Delivered for Claude

TokenShield ships with a **native JSON-RPC 2.0 MCP server** that runs locally over standard input/output (`stdio`).
When Claude is working on your repository, instead of dumping 1,500-line files into Sonnet's context window (**15,000 tokens / $0.045 per query**), Claude calls TokenShield tools via MCP.
TokenShield intercepts the request, queries local RAM in **< 15ms**, and returns a precise 5-line signature and line number (**120 tokens / $0.0003**).

👉 **Net Result:** **84% reduction in Claude Sonnet context bloat**, zero attention dilution, and drastically lower monthly Anthropic bills.

---

## 📦 The 5 Native Claude MCP Tools Delivered

| Tool Name | Parameters | What Claude Receives | Typical Latency |
|---|---|---|---|
| `tokenshield_ref` | `symbol` (string) | Exact typed function/class signature, docstring, and line range | **< 15ms** |
| `tokenshield_diff` | *none* | Surgical unified diffs across modified files (strips unneeded context) | **< 40ms** |
| `tokenshield_lint` | `filepath` (string) | Offline local GPU/CPU syntax and bracket check at **$0.00** | **< 1s** |
| `tokenshield_vault` | `action`: `"push"` \| `"pop"` \| `"list"` \| `"status"` | Preserves and switches in-flight tasks and touched files across conversations | **< 5ms** |
| `tokenshield_status` | *none* | Real-time session token conservation telemetry and quota | **< 1ms** |

---

## 🚀 Setup 1: Claude Desktop Integration

### 1. Locate Your Claude Desktop Config
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

### 2. Add the TokenShield Server Configuration

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

*If you have installed `tokenshield-contextplus` globally via `npm install -g tokenshield-contextplus`, you can also use:*
```json
{
  "mcpServers": {
    "tokenshield": {
      "command": "tokenshield",
      "args": ["mcp"]
    }
  }
}
```

### 3. Restart Claude Desktop
Open Claude Desktop. You will see a hammer icon 🔨 in the chat box showing the 5 active TokenShield tools.

---

## 💻 Setup 2: Claude Code CLI Integration

For Anthropic's official `claude` command-line coding tool:

### 1-Line Command:
```bash
claude mcp add tokenshield npx -y tokenshield-contextplus mcp
```

### Or Manually via `.claude/mcp.json` in Your Project:
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

---

## 🧪 Verification Test: Proving Token Savings

In Claude Desktop or Claude Code, ask:
> *"Use tokenshield_ref to check the function signature of `getProductBySlug` in this workspace."*

### What Happens:
1. Claude dispatches `tokenshield_ref` via JSON-RPC.
2. TokenShield checks the In-RAM SQLite BM25 index in **8ms**.
3. Claude receives only the 5-line definition:
   ```typescript
   export async function getProductBySlug(slug: string, activeOnly: boolean = true): Promise<StoreProduct | null>
   ```
4. Claude completes the task using **118 tokens** instead of reading the 500-line `store-service.ts` file (**5,200 tokens**).
5. Run `npx tokenshield telemetry` to see your token conservation index increment in real time!

---

## 🔒 Enterprise & Commercial Entitlement
The MCP server operates out of the box in **Free Evaluation Mode** (50,000 tokens tracked).  
To unlock unlimited perpetual usage for your team across all repositories:  
👉 **[https://praveenojha.com/tokenshield](https://praveenojha.com/tokenshield)**
