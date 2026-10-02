---
name: zero-any
description: Zero-Any TypeScript & Strict Python Typing Guardian — strictly forbids 'any', 'unknown' casting abuse, untyped dictionary kwargs, and enforces bulletproof static type safety across fullstack codebases.
---

# Zero-Any Strict Typing Guardian Skill (TokenShield)

## Objective & Code Quality Standard
Untyped code (`any`, loose Python `dict`) is the primary driver of silent production runtime failures.
This skill strictly enforces compile-time type safety across TypeScript, JavaScript (JSDoc), and Python.

## Core Directives for AI Agents
1. **Zero `any` in TypeScript:**
   - The `any` keyword is strictly prohibited in TypeScript code.
   - Use generics `<T>`, discriminated unions, or `unknown` combined with type narrowing (`typeof`, `instanceof`, or user-defined type predicates).
   - Use explicit interfaces, types, or Zod schemas for external API responses and message payloads.
2. **Strict Python Type Annotations (PEP 484 / PEP 526):**
   - Every function signature must have explicit argument types and return type annotations:
     ```python
     def process_metrics(session_id: str, limit: int = 50) -> dict[str, int]:
     ```
   - Avoid generic `dict` or `**kwargs` for structured data; use `TypedDict`, `dataclasses`, or `pydantic.BaseModel`.
3. **Verify Static Types Before Finishing:**
   - In TypeScript projects: Run `npx tsc --noEmit` to confirm zero type errors.
   - In Python projects: Verify clean imports and types with `python3 -m py_compile <file>` or `mypy`.
