# Inspector knowledge pipeline (demo)

A test of one idea: when `kb-platform-demo` changes, Claude Code updates this agent's skills and
opens a pull request for a person to review. Everything here is made up.

- `skills/`: the agent's knowledge, in the Agent Skills format (`SKILL.md` with `name` and
  `description`).
- `scripts/check_skills.py`: the format check every change must pass.
- `.github/workflows/update-knowledge.yml`: runs when `kb-platform-demo` sends a
  `repository_dispatch` event. Claude is called through AWS Bedrock with a short-lived role that
  can only call one model.
