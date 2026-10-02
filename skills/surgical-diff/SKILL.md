---
name: surgical-diff
description: Surgical Diff & Token Economizer — instructs AI agents to emit surgical 3-line unified diff chunks and invoke tokenshield diff rather than rewriting entire files, saving 70% to 95% on context tokens.
---

# Surgical Diff & Token Economizer Skill (TokenShield)

## Objective & Economic Impact
Rewriting full files to modify 5 lines is the single biggest cause of context window overflow, high latency, and cloud API bill inflation.
This skill commands AI agents to use surgical diffing, saving **70% to 95%** of context tokens on every file modification.

## Core Directives for AI Agents
1. **Never Output Whole Files for Minor Changes:**
   - If modifying an existing file, output only the modified block or unified diff (`diff -u`) with at most 3 lines of context.
   - Use surgical replacement tools (`replace_file_content` / `multi_replace_file_content`) specifying start/end lines and exact target content.
2. **Powered by TokenShield Diff Economizer:**
   - Execute `tokenshield diff` (or call MCP tool `tokenshield_diff`) to view lean diffs and verify token conservation.
   - Run `tokenshield diff <filepath>` to see exact modifications and calculated percentage savings.
3. **Pre-Flight Local Syntax Validation:**
   - After applying surgical diffs, run `tokenshield lint <filepath>` (or call MCP tool `tokenshield_lint`) to verify syntax and bracket matching in < 1s with 0 cloud tokens.
4. **Collision-Free Patch Verification:**
   - Before applying git patches, test them with `git apply --check` to guarantee zero merge conflicts.
