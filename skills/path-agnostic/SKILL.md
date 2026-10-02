---
name: path-agnostic
description: Path-Agnostic & Serverless Portability Sentry — prevents hardcoding absolute filesystem paths, ensuring code runs seamlessly across Vercel serverless, Docker containers, Windows, Linux, and macOS.
---

# Path-Agnostic & Serverless Portability Sentry Skill (TokenShield)

## Objective & Portability Standard
Hardcoding developer machine paths (e.g. `/home/praveen/...`, `C:\Users\...`) causes instant build breakages in CI/CD, Docker containers, and serverless hosting environments (Vercel, AWS Lambda, Cloudflare Workers).

## Core Directives for AI Agents
1. **Never Hardcode Absolute Host Paths:**
   - Strictly forbidden: `/home/...`, `C:\...`, `/Users/...`, `/tmp/...`.
   - Node.js / Next.js: Always resolve relative to current execution context via `process.cwd()` or `path.join(__dirname, ...)`.
   - Python: Always use `os.path.dirname(os.path.abspath(__file__))` or `pathlib.Path(__file__).parent.resolve()`.
2. **Environment Variable Fallbacks:**
   - For configurable storage locations, always read from environment variables with safe relative defaults:
     ```javascript
     const dataDir = process.env.DATA_DIR || path.join(process.cwd(), 'data');
     ```
3. **Cross-Platform Path Normalization:**
   - Always normalize paths using forward slashes (`/`) or `path.posix` for keys, database records, and URLs to prevent Windows backslash escaping errors.
