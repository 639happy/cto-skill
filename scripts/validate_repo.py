#!/usr/bin/env python3
"""Validate the public CTO Skill package without third-party dependencies."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "ctoskill"

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "THIRD_PARTY_NOTICES.md",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "context-and-adr.md",
    SKILL_DIR / "references" / "cto-brief-template.md",
    SKILL_DIR / "references" / "risk-triggers.md",
    SKILL_DIR / "references" / "superpowers-handoff.md",
)

BLOCKED_PUBLIC_DIRECTORIES = ("/.superpowers/", "/docs/", "/evals/")
SENSITIVE_PATTERNS = {
    "macOS user path": re.compile("/" + r"Users/[^/\s]+/"),
    "private key": re.compile(r"BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]+"),
    "generic bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}", re.I),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


for required in REQUIRED_FILES:
    if not required.is_file():
        fail(f"missing required file: {required.relative_to(ROOT)}")

skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
parts = skill_text.split("---", 2)
if len(parts) != 3 or parts[0].strip():
    fail("SKILL.md must start with YAML frontmatter")

frontmatter = parts[1]
metadata_keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter, flags=re.M)
if metadata_keys != ["name", "description"]:
    fail("SKILL.md frontmatter must contain only name and description")
if not re.search(r"^name:\s*ctoskill\s*$", frontmatter, flags=re.M):
    fail("SKILL.md name must be ctoskill")
if len(skill_text.splitlines()) >= 500:
    fail("SKILL.md must stay below 500 lines")

for reference in re.findall(r"\]\((references/[^)]+\.md)\)", skill_text):
    if not (SKILL_DIR / reference).is_file():
        fail(f"broken SKILL.md reference: {reference}")

openai_text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
for required_text in (
    'display_name: "CTO Skill｜把软件想法问清楚"',
    "使用 $ctoskill",
    "allow_implicit_invocation: false",
):
    if required_text not in openai_text:
        fail(f"openai.yaml is missing: {required_text}")

plain_language_blocklist = (
    "轻量外层编排器",
    "Intake 合同",
    "Handoff 与返回合同",
    "triggered risk preflight",
    "Phase 0",
    "canonical",
    "幂等",
    "readiness review",
)
for blocked_term in plain_language_blocklist:
    if blocked_term in skill_text:
        fail(f"SKILL.md contains unexplained developer wording: {blocked_term}")

readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
for platform_name in ("Codex", "Claude Code", "Cursor", "Windsurf", "WorkBuddy"):
    if platform_name not in readme_text:
        fail(f"README.md is missing platform guidance: {platform_name}")
if "Agent Skills 格式" not in readme_text:
    fail("README.md must explain the portable Agent Skills core")

gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
for blocked_directory in BLOCKED_PUBLIC_DIRECTORIES:
    if blocked_directory not in gitignore:
        fail(f".gitignore must exclude internal directory: {blocked_directory}")

if (ROOT / ".git").exists():
    tracked = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    for path in tracked:
        if path.startswith((".superpowers/", "docs/", "evals/")):
            fail(f"internal artifact must not be tracked: {path}")

public_files = [
    path
    for path in ROOT.rglob("*")
    if path.is_file()
    and ".git" not in path.parts
    and not any(part in {".superpowers", "docs", "evals", "__pycache__"} for part in path.parts)
]
for path in public_files:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, pattern in SENSITIVE_PATTERNS.items():
        if pattern.search(text):
            fail(f"{label} found in {path.relative_to(ROOT)}")

notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
for attribution in ("Copyright (c) 2026 Matt Pocock", "Copyright (c) 2025 Jesse Vincent"):
    if attribution not in notices:
        fail(f"missing third-party attribution: {attribution}")

print(f"PASS: validated {len(public_files)} public files")
