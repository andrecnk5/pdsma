#!/usr/bin/env python3
"""Validação local de estrutura e links relativos; não verifica verdade técnica."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

root = Path(__file__).resolve().parent.parent
errors = []
links = re.compile(r"!?(?:\[[^]]*\])\(([^)]+)\)")
headings = re.compile(r"(?m)^# ")
files = [p for p in root.rglob("*.md") if ".git" not in p.parts]
required = ["README.md", "CONTRIBUTING.md", "CHANGELOG.md", "docs/02-fluxo-e-controles.md"]
for item in required:
    if not (root / item).is_file():
        errors.append(f"Falta arquivo: {item}")
for file in files:
    text = file.read_text(encoding="utf-8")
    if len(headings.findall(text)) != 1:
        errors.append(f"{file.relative_to(root)}: esperado um único H1")
    if not text.endswith("\n"):
        errors.append(f"{file.relative_to(root)}: falta newline final")
    for match in links.finditer(text):
        url = match.group(1).strip().split(" ", 1)[0].strip("<>")
        if not url or url.startswith(("http://", "https://", "#", "mailto:", "tel:")):
            continue
        target = unquote(url.split("#", 1)[0])
        if not target:
            continue
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        resolved = (file.parent / target).resolve()
        if root not in resolved.parents and root != resolved:
            errors.append(f"{file.relative_to(root)}: link fora do projeto: {url}")
        elif not resolved.exists():
            errors.append(f"{file.relative_to(root)}: link ausente: {url}")
if errors:
    print("\n".join("ERRO: " + e for e in errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(files)} arquivos Markdown revisados para estrutura/links locais.")
