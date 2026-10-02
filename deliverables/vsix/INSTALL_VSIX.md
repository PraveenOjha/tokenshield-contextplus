# TokenShield ContextPlus — VS Code & Cursor Extension (.vsix)

## Deliverable File
- **VSIX Package:** [`tokenshield-contextplus-1.0.8.vsix`](file:///home/praveen/Desktop/work/portfolio-engine/portfolioEngine/deliverables/vsix/tokenshield-contextplus-1.0.8.vsix)

---

## 1-Click Installation Instructions

### Method A: VS Code / Cursor / Windsurf GUI (Drag & Drop)
1. Open **VS Code**, **Cursor**, or **Windsurf**.
2. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS) to open the **Extensions** view.
3. Click the **`...` (Views and More Actions)** menu at the top right of the Extensions panel.
4. Select **Install from VSIX...**
5. Pick `tokenshield-contextplus-1.0.8.vsix`.

### Method B: Terminal Command Line (Instant)
```bash
# For VS Code:
code --install-extension deliverables/vsix/tokenshield-contextplus-1.0.8.vsix

# For Cursor:
cursor --install-extension deliverables/vsix/tokenshield-contextplus-1.0.8.vsix

# For Windsurf:
windsurf --install-extension deliverables/vsix/tokenshield-contextplus-1.0.8.vsix
```

---

## Zero-Touch First Launch & Auto-Detection Behavior

When installed on any machine, the extension runs `autoBootstrapEnvironment()` on activation:

1. **Node.js Check:** Built-in! The extension runs natively inside the editor's Node.js runtime, so no separate Node setup is required.
2. **Python Check:** Automatically probes `python3`, `python`, or `py`. All core scripts strictly use the **Python standard library** (`sqlite3`, `socket`, `hashlib`, `urllib`, `json`, `subprocess`). **Zero `pip install` packages are required!**
3. **LM Studio / Local GPU Check:** Automatically probes `http://127.0.0.1:1234/v1` (LM Studio) and `http://127.0.0.1:11434/api` (Ollama).
   - If LM Studio is running, it connects and leverages local GPU inference (0 API token cost).
   - If LM Studio is not running, it **seamlessly falls back to ultra-fast native In-RAM SQLite BM25 indexing (<2ms)** without any error or stall!
4. **Auto-Initialization:** Automatically creates the workspace `.agents/.rag_memory.db` index on first run if missing.
5. **Status Bar & Command Palette:**
   - Displays `🛡️ TokenShield: ON` in the status bar.
   - Adds commands: `TokenShield: Toggle Shield`, `TokenShield: Find Symbol References (In-RAM AST)`, `TokenShield: Show Live Telemetry`, `TokenShield: Select Local LLM Model`.
