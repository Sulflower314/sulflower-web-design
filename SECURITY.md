# Security Policy

## Supported versions

Security fixes are applied to the latest released version.

## Reporting a vulnerability

Do not publish credentials, tokens, private URLs, personal data, or exploitable details in a public issue. Use GitHub's private vulnerability reporting feature when it is enabled for the repository. If private reporting is unavailable, contact the repository owner through a non-public GitHub channel and provide only the information needed to reproduce the problem safely.

## Scope

Relevant reports include:

- instructions that encourage credential or private-data exposure;
- unsafe asset or dependency sourcing;
- code examples that enable injection or unsafe script execution;
- publishing workflows that leak private filesystem paths or internal URLs;
- packaged secrets or sensitive metadata.

This project is an instruction package rather than a hosted service. Vulnerabilities in generated applications should also be reported to the maintainers of those applications and dependencies.
