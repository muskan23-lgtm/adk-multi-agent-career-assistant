"""Skill Gap Agent for finding missing skills."""


class SkillGapAgent:
    """Identify skills found in the job description but not in the resume."""

    def find_gaps(self, resume_info: dict, job_match_info: dict) -> dict:
        """Return missing skills and learning suggestions."""
        resume_skills = set(resume_info.get("skills", []))
        job_skills = set(job_match_info.get("job_skills", []))

        # Missing skills are required by the job but absent from the resume.
        missing_skills = sorted(job_skills.difference(resume_skills))

        # Give one simple suggestion for each missing skill.
        learning_plan = [
            f"Learn or practice {skill} with a small portfolio project."
            for skill in missing_skills
        ]

        return {
            "missing_skills": missing_skills,
            "learning_plan": learning_plan,
        }

