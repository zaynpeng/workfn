# WorkFn

> Turn workplace judgment into reusable skills.

WorkFn is a function-style workplace Skill library for structured judgment, risk checks, and reusable workflows.

WorkFn is not a universal workplace chatbot.
Each Skill solves one clearly defined workplace problem.
A Skill checks inputs, evidence, risks, and boundaries before producing an output.

Every WorkFn Skill first performs parameter parsing and completeness checks. A Skill does not immediately generate an answer. It first identifies which parameters the user has provided, which are missing or conflicting, and whether the available information supports reliable analysis. See [SKILL_RUNTIME_PROTOCOL.md](SKILL_RUNTIME_PROTOCOL.md).

## Naming

Skills use uppercase function-style display names such as `REPLY()`, `RFQ()`, and `FOLLOWUP()`. Their directories use lowercase names without parentheses, such as `reply`, `rfq`, and `followup`.

Each WorkFn Skill has a unique publishable Skill ID using the `zayn-` prefix.

Example:

- Skill ID: `zayn-reply`
- Display Name: `REPLY()`
- Chinese Name: 客户回复

The Skill ID is intended for future publishing and brand identification. This does not claim compatibility with any specific platform. Existing directory names remain unchanged until target-platform requirements are confirmed.

## Current stage

Version `v0.1.0` is a local, publication-ready documentation scaffold. The Skill folders and standard documents exist, but detailed business rules, validated examples, tests, and platform compatibility are not complete.

## Skill index

See [SKILL_INDEX.md](SKILL_INDEX.md) for the complete catalog and priorities.

## Repository structure

- Ten numbered categories contain 51 indexed Skills.
- The project-level orchestration Skill is stored under `00_skill_orchestration/route/`.
- Alibaba-specific Skills are stored under `08_platform_specific/alibaba/`.
- Product Intelligence is stored under `09_product_intelligence/`.
- Each Skill contains `README.md`, `SKILL.md`, `examples.md`, `tests.md`, and `changelog.md`.
- `templates/` contains reusable document skeletons.
- `platform_adapters/` reserves space for verified platform-specific requirements.

## Skill orchestration

`ROUTE()` is the orchestration layer of WorkFn.

It identifies the problem, selects the appropriate Skills, defines the execution order, passes only necessary outputs, and sets stop conditions. It does not automatically execute other Skills.

## Development order

1. Complete and review one Skill's requirements.
2. Add confirmed examples and risk cases.
3. Add acceptance tests.
4. Review evidence rules and human-judgment boundaries.
5. Only then prepare a platform adapter and release.

The first planned Skills are `REPLY()`, `RFQ()`, and `FOLLOWUP()`.

New skeletons include `INTENT_DECODE()`, `KEYPOINT()`, and `ORDER_KICKOFF()`.

## Not included

This repository currently contains no frontend, database, automation framework, runtime invocation logic, verified WorkBuddy adapter, remote repository, release, or confirmed license.

## 中文文档

See [README.zh-CN.md](README.zh-CN.md).

## Suggested GitHub metadata

- Repository name: `workfn-skills`
- Display name: `WorkFn`
- Description: `A function-style workplace Skill library for structured judgment, risk checks, and reusable workflows.`
- Suggested topics: `ai-skills`, `workplace`, `productivity`, `sales`, `communication`, `prompt-engineering`, `workflow`, `knowledge-management`
- Suggested first release: `v0.1.0`

These are publication suggestions only. No remote repository or release has been created.
