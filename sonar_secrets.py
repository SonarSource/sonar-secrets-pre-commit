#!/usr/bin/env python3
# sonar-secrets.py
#
# SPDX-FileCopyrightText: 2025 SonarSource SàrL
#
# SPDX-License-Identifier: LicenseRef-SonarSource-SSAL-1.0
#

import os
import platform
import stat
import subprocess
import sys
import urllib.request
import urllib.error

# --- Configuration ---
# The version used in the download URL tag
TAG_VERSION = "2.41.0.10709"
# The full version used in the binary filenames
BINARY_VERSION = TAG_VERSION
# GitHub repository details
REPO_OWNER = "SonarSource"
REPO_NAME = "sonar-secrets-pre-commit"
# ---------------------

def get_target_binary_name():
    """Detects the OS and architecture to determine the target binary name."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "linux":
        if "arm" in machine or "aarch64" in machine:
            platform_id = "linux-arm64"
        else:
            platform_id = "linux-x86-64"
    elif system == "darwin" and ("arm" in machine or "aarch64" in machine):
        platform_id = "macos-arm64"
    elif system == "windows":
        platform_id = "windows-x86-64.exe"
    else:
        print(f"Error: Unsupported system/architecture combination: {system}/{machine}", file=sys.stderr)
        print("Supported platforms: Linux (x86-64, ARM64), Windows (x86-64), macOS (ARM64)", file=sys.stderr)
        sys.exit(1)
        
    return f"sonar-secrets-{BINARY_VERSION}-{platform_id}"

def get_home_directory():
    """Get the user's home directory in a cross-platform way."""
    # On Windows, prefer USERPROFILE, fallback to HOMEDRIVE + HOMEPATH
    if platform.system() == "Windows":
        home = os.environ.get('USERPROFILE')
        if not home:
            home_drive = os.environ.get('HOMEDRIVE', '')
            home_path = os.environ.get('HOMEPATH', '')
            home = os.path.join(home_drive, home_path)
        return home
    else:
        # On Unix-like systems, use the standard approach
        return os.path.expanduser("~")

def download_binary(target_binary, executable_path):
    """Download the binary directly from GitHub releases."""
    download_url = (
        f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/download/"
        f"v{TAG_VERSION}/{target_binary}"
    )

    print(f"Downloading Sonar Secrets binary from '{download_url}'...", file=sys.stderr)
    try:
        req = urllib.request.Request(download_url)
        with urllib.request.urlopen(req) as response, open(executable_path, 'wb') as out_file:
            out_file.write(response.read())
    except urllib.error.URLError as e:
        print(f"Error: Failed to download binary: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main script logic."""
    target_binary = get_target_binary_name()
    
    # Use a .sonar directory for binary cache
    home_dir = get_home_directory()
    sonar_cache_dir = os.path.join(home_dir, ".sonar")
    binary_cache_dir = os.path.join(sonar_cache_dir, "binary_cache", BINARY_VERSION)
    
    os.makedirs(binary_cache_dir, exist_ok=True)
    
    executable_path = os.path.join(binary_cache_dir, target_binary)
    
    # Download the binary if it's not in our cache
    if not os.path.exists(executable_path):
        download_binary(target_binary, executable_path)

    # Ensure the binary is executable (for Linux/macOS)
    if platform.system() != "Windows":
        st = os.stat(executable_path)
        os.chmod(executable_path, st.st_mode | stat.S_IEXEC)

    # Run the binary with the arguments passed by pre-commit
    try:
        result = subprocess.run([executable_path] + sys.argv[1:], check=False)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"Error: Failed to execute sonar-secrets binary: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
