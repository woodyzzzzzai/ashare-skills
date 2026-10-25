#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
paths = list(ROOT.glob("*/SKILL.md"))
assert len(paths) == 37, len(paths)
for p in paths:
    text = p.read_text()
    assert text.startswith("---\n"), p
    data = yaml.safe_load(text.split("---", 2)[1])
    assert data["name"] == "ashare-" + p.parent.name and data["description"], p
    assert (p.parent / "../references/data-contract.md").is_file()
    yaml.safe_load((p.parent / "agents/openai.yaml").read_text())
print("PASS: 37 A-share skills, frontmatter, shared references and agent YAML")
