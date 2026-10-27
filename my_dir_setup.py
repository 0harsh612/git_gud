"""
Setup script to initialize your personal solutions directory for Git Gud Workshop.

Run this script after forking and cloning the repo:
    python my_dir_setup.py

It will automatically detect your GitHub username from your git remote origin
and create a dedicated workspace under SOLUTIONS/<username>_solutions containing
a copy of the arena challenges!
"""

import pathlib
import subprocess
import shutil
import sys

# Ensure UTF-8 output on Windows consoles if supported
if sys.platform.startswith("win"):
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def get_git_owner(git_root: pathlib.Path) -> str:
    """Retrieve repository owner from git remote or local git config."""
    try:
        remote_url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            cwd=str(git_root),
            stderr=subprocess.STDOUT
        ).decode("utf-8", errors="replace").strip()

        # Parse owner from URL formats:
        # https://github.com/owner/repo.git or git@github.com:owner/repo.git
        if "github.com" in remote_url:
            if remote_url.startswith("http"):
                owner = remote_url.split("github.com/")[1].split("/")[0]
            else:
                owner = remote_url.split("github.com:")[1].split("/")[0]
            return owner
    except Exception:
        pass

    # Fallback to git config user.name if origin is not a github url
    try:
        user_name = subprocess.check_output(
            ["git", "config", "user.name"],
            cwd=str(git_root),
            stderr=subprocess.STDOUT
        ).decode("utf-8", errors="replace").strip()
        if user_name:
            clean_name = "".join(c for c in user_name if c.isalnum() or c in ("-", "_"))
            if clean_name:
                return clean_name
    except Exception:
        pass

    return None


def setup_solutions():
    current_file = pathlib.Path(__file__).resolve()
    current_dir = current_file.parent

    # Find git root
    git_root = None
    for parent in [current_dir] + list(current_file.parents):
        if (parent / ".git").exists():
            git_root = parent
            break

    if not git_root:
        print("[!] Error: Not inside a git repository.")
        sys.exit(1)

    owner = get_git_owner(git_root)
    if not owner:
        print("[!] Warning: Could not detect GitHub username from git remote or git config.")
        owner = input(">> Enter your GitHub username: ").strip()
        if not owner:
            print("[!] Error: Username cannot be empty.")
            sys.exit(1)

    # Ensure SOLUTIONS directory exists
    solutions_dir = current_dir / "SOLUTIONS"
    solutions_dir.mkdir(parents=True, exist_ok=True)

    target_folder_name = f"{owner}_solutions"
    target_path = solutions_dir / target_folder_name

    if target_path.exists():
        print(f"[*] Directory 'SOLUTIONS/{target_folder_name}' already exists.")
        print("[*] You are all set to work inside your personal solutions directory!")
        return

    # Find arena source directory
    arena_src = current_dir / "arena"
    if not arena_src.exists():
        arena_src = current_dir / "test_playground"
    
    if not arena_src.exists():
        print("[!] Error: 'arena' directory not found to copy from.")
        sys.exit(1)

    try:
        shutil.copytree(arena_src, target_path)
        print(f"[+] Successfully created 'SOLUTIONS/{target_folder_name}'!")
        print(f"[+] Copied arena challenges into your personal solutions directory.")
        print(f"[+] Have fun hacking on the puzzles and tasks in: SOLUTIONS/{target_folder_name}/")
    except Exception as e:
        print(f"[!] An error occurred during setup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    setup_solutions()

