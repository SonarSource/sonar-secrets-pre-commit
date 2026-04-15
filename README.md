# SonarSecrets CLI Pre-Commit Hook

> [!WARNING]
> The pre-commit hook in this repository is deprecated and will be archived.
> 
> Please use the [sonarqube-cli](https://github.com/SonarSource/sonarqube-cli) instead.
> 
> With the `sonarqube-cli` you're able to install the secrets analysis as a local (and global) pre-commit hook.
> 
> Additionally you can integrate the secrets analysis into Claude Code with the help of the `sonarqube-cli`, and even more integrations are planned for the future.

## Overview

This repository hosts **SonarSecrets CLI** binaries for use in pre-commit hooks, enabling detection of secrets before code is committed.

**Important:** The **SonarSecrets Pre-Commit Hook** is currently in ![alpha](https://img.shields.io/badge/status-alpha-orange).

Using the SonarSecrets CLI outside of the pre-commit hook context is **not authorized** and **not supported**.

The **SonarSecrets CLI Pre-Commit Hook** integrates with your local Git workflow to automatically scan staged changes for potential secrets (such as API keys, passwords, or tokens) before they are committed.

This helps prevent accidental leakage of sensitive information into your codebase or version control history.


## Installation

Note: if you're a SonarSourcer, see the internal ["How to install "sonar-secrets" CLI as a pre-commit hook?"](https://docs.google.com/document/d/1OKY4dlcn5o_QHlMa3lXtQXPg3hrl4hz-4NBPXbGG37M/edit?tab=t.0#heading=h.yhp1i1g0e22v)

The [pre-commit](https://pre-commit.com/) framework is required.

Create in the root directory of your Git repository a `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: https://github.com/SonarSource/sonar-secrets-pre-commit
    rev: v2.41.0.10709
    hooks:
    -   id: sonar-secrets
        stages: [pre-commit]
```

Then run:
```bash
pre-commit autoupdate
pre-commit uninstall
pre-commit clean
pre-commit install
```

## Set Up Authentication

Authentication to a SonarQube Server instance or to SonarQube Cloud is required.
It can be done by setting 2 environment variables.

For SonarQube Server:
- `SONAR_SECRETS_AUTH_URL`: the URL of your SonarQube instance (e.g., https://example.sonarqube.com)
- `SONAR_SECRETS_TOKEN`: a token of any type (can be created at "/account/security")

For SonarQube Cloud:
- `SONAR_SECRETS_AUTH_URL`: the URL of a SonarQube Cloud (e.g., https://sonarcloud.io)
- `SONAR_SECRETS_TOKEN`: a token (e.g., can be created at https://sonarcloud.io/account/security)

Note: the authentication process will be retriggered every 7 days, so these environment variables should be safely persisted.


## Limitations

**Alpha stage**: The hook is still under active development and may change without notice. For more information on disclaimers and warranties on SonarSource's early-access software, see https://www.sonarsource.com/legal/early-access/
**Authorized usage only**: The SonarSecrets CLI is intended solely for use within the pre-commit hook context.
Running the CLI directly or outside of this context is not supported and not authorized.

## License

Copyright 2025 SonarSource SàrL

Scripts licensed under the [SONAR Source-Available License](https://www.sonarsource.com/license/ssal/)

Binaries licensed to Sonar customers under SonarSource's commercial terms, solely for use in pre-commit hooks. See [SonarSource's Legal pages for more information](https://www.sonarsource.com/legal/).
