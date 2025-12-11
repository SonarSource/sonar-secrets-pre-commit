#!/usr/bin/env python3
# setup.py
#
# SPDX-FileCopyrightText: 2025 SonarSource SàrL
#
# SPDX-License-Identifier: LicenseRef-SonarSource-SSAL-1.0
#

from setuptools import setup

from sonar_secrets import BINARY_VERSION

setup(
    name="sonar-secrets-hook",
    version=BINARY_VERSION,
    py_modules=["sonar_secrets"],
    entry_points={
        "console_scripts": [
            "sonar-secrets = sonar_secrets:main",
        ],
    },
)
