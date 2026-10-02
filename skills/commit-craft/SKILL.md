---
name: commit-craft
description: Conventional Commit & Secret Sentry — crafts crystal-clear, standardized git commit messages and PR summaries while scanning diffs for leaked secrets, API keys, and environment tokens.
---

# Conventional Commit & Secret Sentry Skill (TokenShield)

## Objective & Security Standard
Ensures every git commit is clean, traceable, follows the Conventional Commits specification, and is guaranteed 100% free of leaked secrets or credentials.

## Core Directives for AI Agents
1. **Conventional Commits Standard:**
   - Format: `<type>(<scope>): <short imperative description>`
   - Allowed Types:
     - `feat`: A new user-facing feature or capability
     - `fix`: A bug fix or crash resolution
     - `refactor`: Code restructuring with zero behavioral change
     - `perf`: Performance or token-saving optimization
     - `docs`: Documentation, README, or markdown updates
     - `chore`: Tooling, dependency updates, or internal scripts
2. **Secret & Key Leak Prevention:**
   - Scan staged changes before committing:
     - Never commit `.env`, `.env.local`, API keys (`sk-...`, `Bearer ...`, private tokens, RSA keys).
     - Ensure secrets are stored in `.gitignore` or local secret managers.
3. **Structured Commit Body:**
   - Include what changed, why it changed, and what was verified (e.g. `Tested: 19/19 passing`).
