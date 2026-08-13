# Sulflower Web Design

An open-source frontend-design skill for AI coding agents. It helps agents create, extend, reconstruct, improve, and critique polished browser interfaces while respecting the framework, components, tokens, and engineering constraints of an existing codebase.

[中文](README.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT License](LICENSE)

## Highlights

- Four work modes: Create, Extend, Reconstruct, and Improve.
- Preserved brand-first color practice, `oklch()` derivation, and semantic color systems.
- Preserved typography, whitespace, hierarchy, motion, and anti-cliché design rules.
- Twenty-five progressively loaded style recipes.
- Works with semantic HTML/CSS/JavaScript, portable React prototypes, and repository-native frontend stacks.
- Adds brand-asset rights, responsive QA, accessibility, performance, and delivery verification.
- Keeps the main skill concise by routing detailed guidance to task-specific references.

## Install

### One-command install (Windows PowerShell)

After reviewing and trusting this repository, run the following command. It downloads the latest version from GitHub and installs it into the current user's Codex skill directory:

```powershell
irm https://raw.githubusercontent.com/Sulflower314/sulflower-web-design/main/install.ps1 | iex
```

Restart Codex or reload your skills before using `$sulflower-web-design`.

If the target directory already exists, installation overwrites files with the same names. Back up local changes first if needed.

If you prefer to inspect the script first, download it and run it locally:

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/Sulflower314/sulflower-web-design/main/install.ps1 -OutFile .\install.ps1
Get-Content .\install.ps1
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### Manual installation

If you already downloaded or cloned this repository, copy the complete `skill/sulflower-web-design/` directory to a skill path supported by your agent. The commands below must run from the repository root; they do not download the skill directly from GitHub.

For a Codex user-level installation on macOS or Linux:

```bash
cp -R skill/sulflower-web-design ~/.codex/skills/sulflower-web-design
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse -Force .\skill\sulflower-web-design "$env:USERPROFILE\.codex\skills\sulflower-web-design"
```

For tools that support project-level skills, copy it to:

```text
your-project/.agents/skills/sulflower-web-design/
```

Check the current documentation for your agent because discovery paths may differ.

## Use

```text
Use $sulflower-web-design to add a responsive analytics page that matches this existing React product.
```

```text
Use $sulflower-web-design to reconstruct this supplied design frame without changing its visual language.
```

```text
Use $sulflower-web-design to critique this interface's hierarchy, interaction states, and accessibility.
```

## Repository layout

The directly installable skill lives at `skill/sulflower-web-design/`. Repository-level documentation remains outside the skill so it does not consume agent context during normal use.

## License and provenance

This project is an independently maintained MIT-licensed adaptation. Sulflower maintains the 2.0 workflow modes, repository integration, confirmation policy, accessibility, performance, asset-rights, QA, and open-source packaging while retaining the established visual-design and color foundations.

See [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE).
