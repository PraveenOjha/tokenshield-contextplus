# 🛡️ TokenShield & Context++ Changelog

All notable changes, architectural refactors, and diagnostic enhancements to **TokenShield & Context++** are documented in this file.

---

## [1.0.7] - 2026-10-02

### 🔒 Zero-PII Privacy & Local-Only Guarantee
- **Complete Local Execution**:
  - 100% of AST Call-Graph parsing, In-RAM SQLite BM25 indexing, surgical diff economizing, chat archiving, and syntax validation run locally on device.
  - **Zero proprietary source code, zero file paths, zero git commits, zero prompts, and zero developer logs ever leave your system.**
- **Anonymous Community Counter**:
  - Outbound telemetry is strictly restricted to an anonymous aggregate payload:
    ```json
    { "tokens_saved": 48200, "ide": "vscode" }
    ```
  - Shared with `praveenojha.com` exclusively to power the live public community token savings ticker on the boutique store.

### 💻 Universal Multi-IDE Hub & Auto-Registration
- **Cross-IDE Native Integration**:
  - Auto-configures and arms across **VS Code**, **Cursor**, **Windsurf**, **Claude Desktop**, **Claude Code CLI**, **Gemini / Antigravity**, and **JetBrains / Terminal**.
  - Single command `npx tokenshield setup-mcp` auto-detects installed environments and registers MCP JSON-RPC bridges in < 50ms.

### 🎙️ Universal Zero-Pip Whisper STT & Audio Guard
- **Standalone `whisper.cpp` Integration**:
  - Lightweight C/C++ engine (`~/.tokenshield/tools/whisper-cli` + `ggml-tiny.bin`) executes offline speech-to-text in < 200ms.
  - **Zero pip / PyTorch dependencies**: Eliminates 2.5GB CUDA wheel downloads and runs seamlessly across Windows (`.exe`), macOS (Metal), and Linux (`x86_64`/`arm64`).
  - Added `tokenshield install-whisper` and `tokenshield audio` CLI commands.

### 🔓 Device License Delink / Unbind Action
- **Dynamic Seat Portability**:
  - Added dedicated **`🔓 Unbind License From This Device`** button in the Extension Dashboard (Tab 4: License & Quota).
  - Added `TokenShield: Unbind / Delink License From This Device` to the VS Code Command Palette.
  - Cryptographically notifies the central license authority to free the active machine seat so developers can transfer licenses between devices.

### 🏷️ Brand & Entity Alignment
- **Praveen Ojha Copyright & Support**:
  - Replaced company designation with **Praveen Ojha** (`© 2026 Praveen Ojha. All rights reserved. Support: support@praveenojha.com`), recognizing PortSync as a product.

---

## [1.0.6] - 2026-10-02

### 📁 Workspace & Custom Folder RAG Memory Ingestion
- **Full-Workspace File Consumption (Non-Binary)**:
  - Removed restrictive source-code-only extension filters in `agent_ram_rag.py`.
  - TokenShield now automatically ingests **100% of all workspace files** (Markdown documents, prompts, SQL schemas, YAML configs, JSON schemas, shell scripts) up to 500KB into In-RAM SQLite FTS5 BM25.
  - Excludes only compiled/binary assets (`.png`, `.jpg`, `.zip`, `.pyc`, `.dll`, `.wasm`, etc.).
- **Dynamic Custom Folder Addition (`/folder`)**:
  - Implemented `tokenshield add-folder <path>` (alias: `tokenshield folder add <path>`), `tokenshield remove-folder <path>`, and `tokenshield folders`.
  - Persists external directories in `.agents/extra_rag_folders.json` and `~/.tokenshield/extra_rag_folders.json` for persistent multi-folder RAG.
- **Extension Dashboard Folder Manager (Sidebar Webview)**:
  - Added dedicated **Indexed Folders & Workspace Memory** card to the Extension Webview Dashboard (Memory Tab).
  - Features real-time folder matrix with file/symbol counts and `WORKSPACE REPO` vs `CUSTOM ADDED` status badges.
  - Interactive **📂 Browse** button via native OS picker (`vscode.window.showOpenDialog`) to select any directory.
  - 1-click **⚡ Add & Index Folder** and **🔄 Re-Index Workspace** buttons.
  - 1-click **Remove** action to unbind custom folders and purge their index from SQLite RAM memory.

### 🧠 Dual-Hybrid Dense BGE-M3 & BM25 Auto-Discovery
- **LM Studio Port 1234 Dense Vector Integration**:
  - Automatically queries `http://127.0.0.1:1234/v1/models` for loaded embedding weights (`text-embedding-bge-m3`, `bge-m3`, `nomic-embed-text`).
  - Seamlessly toggles to **Hybrid In-RAM AST & Dense BGE-M3 RAG** when LM Studio has `text-embedding-bge-m3` running, utilizing 1024-dimensional dense semantic vectors.
  - Gracefully falls back to sub-millisecond In-RAM SQLite BM25 (< 15ms, 0 VRAM) whenever LM Studio is closed or offline.
  - Dynamically updates Dashboard chips, status tooltips, and health descriptors (`Dense BGE-M3 + RAM ✓`).

### ⏱️ Chat Checkpoints, Push, Pop & Archiving (`tokenshield archive`)
- **Session Time-Travel & Memory Stashing**:
  - Added dedicated CLI commands and Webview actions:
    - `tokenshield push`: Snapshots current in-flight touched files, goals, and working tasks into `.agents/live_work/stash/`.
    - `tokenshield pop`: Restores the previous session state and touched file list from stack.
    - `tokenshield archive`: Packages active session into `.agents/live_work/archive/session_<timestamp>.json` and resets working context to a clean, fresh state.
    - `tokenshield chats`: Displays a human-friendly numbered list (#1, #2, ...) of all saved chats and archives.
    - `tokenshield load <id>`: Auto-saves active work and instantly restores any historical checkpoint.
- **Context Bloat Prevention**:
  - Massive back-and-forth chat sessions (50k–200k tokens) are never dumped raw into SQLite.
  - `agent_session_compactor.py` and `agent_live_work.py` continuously compress long dialogues into a razor-sharp **< 200 token** state vector (goal, active file, subtasks, decision bullets), eliminating context window degradation.

### 🔐 Dual-Tier Lifetime Pricing & 100k Free Trial Quota
- **Official Dual-Tier Lifetime Licensing Model**:
  - **Personal Indie Pro ($29 USD Lifetime)**: 1 User • 3 Machine Seats (Desktop, Laptop, Cloud VM) with unlimited offline tokens.
  - **Team Agency Pro ($89 USD Lifetime)**: 5 Users • 15 Machine Seats with full multi-dev team fleet synchronization.
  - Cleaned and removed all legacy/test pricing references ($10).
- **100k Free Community Trial Quota**:
  - Strictly normalized all trial allowances across CLI, Webview, License Server, PDF generator, and documentation to **100,000 tokens (100k)**.
  - Removed ambiguous regional terminology.

### 🐍 Python 3 Auto-Installer & System PATH Verification
- **Pre-Flight System PATH Audit**:
  - Added `tokenshield install-python` (and Webview **⚡ Auto-Install (winget/apt)** button).
  - Checks system PATH before executing package managers to avoid redundant installations.
  - Cross-platform support: uses `winget` on Windows, `apt` on Linux, and `brew` on macOS.

### 🌐 Live Model Auto-Detection & Internet Pricing Sync
- **Autonomous Host IDE Environment Sniffing**:
  - Auto-identifies active coding environment: Antigravity IDE (`~/.gemini/antigravity-ide`) defaults to **Google DeepMind Gemini** (`gemini-3.8-flash` / `gemini-2.5-flash`), Claude Code defaults to `claude-3-7-sonnet`, and Cursor/VS Code defaults to Sonnet/GPT-4o.
- **Real-Time Internet Pricing Synchronizer (`tokenshield sync-pricing`)**:
  - Queries public live model registry (`https://openrouter.ai/api/v1/models`) via native HTTPS with zero external npm/pip dependencies.
  - Indexes and updates real-time prompt & completion pricing for **464+ models in < 1s**.
  - Caches live rates locally in `~/.tokenshield/model_pricing_cache.json` with automatic 7-day TTL and resilient offline fallback.

### 🛡️ Audio Input Guard & Strict Standby
- **Strict Audio Format Validation**:
  - Added `is_valid_audio_input()` strictly constraining `audio_context_compressor.py` to genuine audio file extensions (`.wav`, `.mp3`, `.m4a`, `.webm`, `.ogg`, `.flac`, `.aac`, `.opus`).
  - Text prompts, source code files, and non-audio requests immediately return status `idle` with 0 token distortion and zero compute waste.

### 🌐 Anonymous Community Savings Counter (Zero-PII Privacy Guarantee)
- **Zero-Data-Leak Architecture**:
  - 100% of AST Call-Graph parsing, In-RAM SQLite BM25 search, diff economizing, chat archiving, and syntax validation execute completely offline on local developer hardware.
  - **Zero source code, zero file paths, zero git commits, zero prompts, and zero user identifiers ever leave your system.**
- **Anonymous Global Community Counter**:
  - To power the live public token savings counter on `praveenojha.com` and the boutique store, TokenShield sends a single lightweight, anonymous one-time ping:
    ```json
    { "tokens_saved": 48200, "ide": "vscode" }
    ```
  - Developers can be completely confident that only aggregate numeric token counts and the IDE client name are transmitted. No telemetry tracking, no analytics profiling, and no private code leaks.
---

## [1.0.5] - 2026-10-02

### 🚀 Added & Enhanced
- **Full System Diagnostics & Component Health Check (`tokenshield check` & `/check`)**:
  - Implemented 9-point comprehensive diagnostic suite that inspects and reports real-time latency and state for every accelerator.
  - Multi-format output modes: CLI Box Table, Markdown Report (`--markdown`), and Machine JSON (`--json`).
- **Tightened Auto-Initialization & Resilient Failover**:
  - Sub-second parallel socket probes (< 150ms) prevent IDE or terminal blocking during startup.
- **Granular Backend Controls & LM Studio Dropdown Integration**:
  - Added LM Studio as an explicit first-class option in the Webview Dashboard engine dropdown alongside Ollama, vLLM, and Native In-RAM AST.
- **Cumulative Developer Wait-Time Tracking**:
  - Tracks developer time saved (10-30+ hours) by resolving AST references and syntax checks locally in RAM instead of waiting on remote cloud API roundtrips.

---

## [1.0.4] - 2026-10-01

### 🚀 Added
- **Interactive Terminal Control Cockpit (TUI)**: Accessible via `tokenshield tui` or `tokenshield dashboard`.
- **Universal Multi-IDE MCP Auto-Registration**: Zero-touch registration across 6 IDE environments: VS Code, Cursor, Windsurf, Claude Desktop, Claude Code, and Antigravity IDE.
