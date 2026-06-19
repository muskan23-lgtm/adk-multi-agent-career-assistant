"""Job Matching Agent for comparing a resume with a job description."""


class JobMatchingAgent:
    """Compare resume skills against job description skills."""

    def __init__(self) -> None:
        """Create a job matching agent with known job skill keywords."""
        # In a real app, an LLM could extract these from the job description.
        self.skill_keywords = {
            "python": "Python",
            "sql": "SQL",
            "machine learning": "Machine Learning",
            "data analysis": "Data Analysis",
            "pandas": "Pandas",
            "numpy": "NumPy",
            "flask": "Flask",
            "django": "Django",
            "git": "Git",
            "excel": "Excel",
            "communication": "Communication",
            "leadership": "Leadership",
            "tensorflow": "TensorFlow",
            "scikit-learn": "Scikit-learn",
        }

    def compare(self, resume_info: dict, job_description_text: str) -> dict:
        """Compare extracted resume information with a job description."""
        job_skills = self._extract_job_skills(job_description_text)
        resume_skills = set(resume_info.get("skills", []))

        # Matching skills appear in both the resume and the job description.
        matching_skills = sorted(resume_skills.intersection(job_skills))

        # Avoid division by zero if no job skills were found.
        if job_skills:
            match_score = round((len(matching_skills) / len(job_skills)) * 100)
        else:
            match_score = 0

        return {
            "job_skills": sorted(job_skills),
            "matching_skills": matching_skills,
            "match_score": match_score,
        }

    def _extract_job_skills(self, job_description_text: str) -> set[str]:
        """Find skill keywords mentioned in the job description."""
        lower_job_description = job_description_text.lower()

        return {
            display_name
            for keyword, display_name in self.skill_keywords.items()
            if keyword in lower_job_description
        }
