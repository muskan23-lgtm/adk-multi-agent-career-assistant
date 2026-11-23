"""Explainable resume/job-description matching baseline. Not an official ATS score."""

import re
from utils.skill_extractor import extract_skills

STOPWORDS = {
    "and", "the", "for", "with", "from", "that", "this", "will", "your",
    "you", "are", "our", "have", "has", "into", "their", "they", "them",
    "job", "role", "work", "working", "years", "year", "ability", "strong",
    "good", "using", "use", "based", "including", "required", "preferred",
    "responsibilities", "requirements", "candidate"
}

def extract_keywords(text: str) -> set[str]:
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+#./-]{2,}", (text or "").lower())
    return {token for token in tokens if token not in STOPWORDS}

def score_resume_job(resume_text: str, job_description: str) -> dict:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    required = {s.lower() for s in job_skills}
    present = {s.lower() for s in resume_skills}
    matched = sorted([s for s in job_skills if s.lower() in present], key=str.lower)
    missing = sorted([s for s in job_skills if s.lower() not in present], key=str.lower)

    skill_coverage = len(matched) / len(required) if required else 0.0
    resume_words = extract_keywords(resume_text)
    job_words = extract_keywords(job_description)
    keyword_coverage = len(resume_words & job_words) / len(job_words) if job_words else 0.0

    signals = ["internship", "experience", "project", "degree", "bachelor", "master"]
    resume_signals = sum(1 for s in signals if s in (resume_text or "").lower())
    job_signals = sum(1 for s in signals if s in (job_description or "").lower())
    signal_coverage = min(resume_signals / max(job_signals, 1), 1.0)

    score = round(100 * (0.60 * skill_coverage + 0.25 * keyword_coverage + 0.15 * signal_coverage))
    return {
        "score": score,
        "skill_coverage": round(skill_coverage * 100, 1),
        "keyword_coverage": round(keyword_coverage * 100, 1),
        "experience_signal_coverage": round(signal_coverage * 100, 1),
        "matched_skills": matched,
        "not_demonstrated_skills": missing,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_keywords": sorted(resume_words & job_words),
        "note": "Estimated evidence overlap only; not an official ATS score or hiring prediction."
    }
