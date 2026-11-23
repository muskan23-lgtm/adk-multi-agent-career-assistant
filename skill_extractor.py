"""Lightweight skill extraction using an editable skills taxonomy."""

import json
import re
from pathlib import Path

SKILLS_FILE = Path(__file__).resolve().parents[1] / "data" / "skills_database.json"

def load_skills_database() -> dict:
    with SKILLS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower())

def extract_skills(text: str) -> list[str]:
    normalized = _normalize(text)
    found = []
    for category, skills in load_skills_database().items():
        for skill in skills:
            pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
            if re.search(pattern, normalized):
                found.append(skill)
    return sorted(set(found), key=str.lower)

def identify_skill_gaps(candidate_skills: list[str], required_skills: list[str]) -> dict:
    candidate = {s.lower() for s in candidate_skills}
    required = {s.lower() for s in required_skills}
    matched = sorted([s for s in required_skills if s.lower() in candidate], key=str.lower)
    missing = sorted([s for s in required_skills if s.lower() not in candidate], key=str.lower)
    return {"matched_skills": matched, "not_demonstrated": missing}
