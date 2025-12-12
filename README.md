# SonarSecrets CLI Pre-Commit Hook

This repository hosts **SonarSecrets CLI** binaries for use in pre-commit hooks, enabling detection of secrets before code is committed.

**Important:** The **SonarSecrets Pre-Commit Hook** is currently in ![alpha](https://img.shields.io/badge/status-alpha-orange).

Using the SonarSecrets CLI outside of the pre-commit hook context is **not authorized** and **not supported**.

## Overview

The **SonarSecrets CLI Pre-Commit Hook** integrates with your local Git workflow to automatically scan staged changes for potential secrets (such as API keys, passwords, or tokens) before they are committed.

This helps prevent accidental leakage of sensitive information into your codebase or version control history.


## Installation

(internal documentation) See [How to install "sonar-secrets" CLI as a pre-commit hook?](https://docs.google.com/document/d/1OKY4dlcn5o_QHlMa3lXtQXPg3hrl4hz-4NBPXbGG37M/edit?tab=t.0#heading=h.yhp1i1g0e22v) .

## Limitations

**Alpha stage**: The hook is still under active development and may change without notice. For more information on disclaimers and warranties on SonarSource's early-access software, see https://www.sonarsource.com/legal/early-access/
**Authorized usage only**: The SonarSecrets CLI is intended solely for use within the pre-commit hook context.
Running the CLI directly or outside of this context is not supported and not authorized.

## License

Copyright 2025 SonarSource SàrL

Scripts licensed under the [SONAR Source-Available License](https://www.sonarsource.com/license/ssal/)

Binaries licensed to Sonar customers under SonarSource's commercial terms, solely for use in pre-commit hooks. See [SonarSource's Legal pages for more information](https://www.sonarsource.com/legal/).
