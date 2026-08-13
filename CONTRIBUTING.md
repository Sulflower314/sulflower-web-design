# Contributing

Thank you for helping improve Sulflower Web Design.

## Before opening a change

- Search existing issues to avoid duplicate work.
- Explain the user scenario and why the current skill is insufficient.
- Keep visual-design and color changes evidence-based; do not replace the preserved design foundation with personal preference.
- Avoid adding universal rules when a mode-specific or reference-specific rule is sufficient.

## Development guidelines

- Keep `SKILL.md` focused on routing, decisions, hard constraints, and the core workflow.
- Put detailed patterns in `references/` and link them directly from `SKILL.md`.
- Avoid duplicating the same rule across multiple files.
- Keep examples generic and free of private data.
- Add dependencies only when they provide reusable value that browser primitives or the host repository cannot provide.
- Preserve compatibility with agents that support the `SKILL.md` convention.

## Validation

Before submitting a pull request:

1. Validate `skill/sulflower-web-design` with a compatible skill validator.
2. Confirm every referenced file exists.
3. Search for credentials, personal filesystem paths, private URLs, and personal contact data.
4. Verify JSON and YAML syntax.
5. Test the changed workflow against at least one realistic prompt.
6. Describe which checks were run and any limitations.

## Pull requests

Keep each pull request focused. Include:

- the problem being solved;
- the affected mode or reference;
- before/after behavior;
- validation evidence;
- any compatibility or licensing implications.

By contributing, you agree that your contribution may be distributed under the repository's MIT License.
