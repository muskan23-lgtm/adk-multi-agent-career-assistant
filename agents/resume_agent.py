"""Resume Agent for extracting important resume information."""


class ResumeAgent:
    """Extract skills, education, projects, and experience from resume text."""

    def __init__(self) -> None:
        """Create a resume agent with common skill keywords."""
        # These keywords keep the example simple and beginner friendly.
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

    def extract_information(self, resume_text: str) -> dict:
        """Return a dictionary with extracted resume details."""
        lower_resume = resume_text.lower()

        # Find skills by checking whether each keyword appears in the resume.
        skills = [
            display_name
            for keyword, display_name in self.skill_keywords.items()
            if keyword in lower_resume
        ]

        # These helper methods keep the main extraction method easy to read.
        education = self._find_lines_with_keywords(
            resume_text,
            ["degree", "bachelor", "master", "university", "college"],
        )
        projects = self._find_lines_with_keywords(
            resume_text,
            ["project", "built", "created", "developed"],
        )
        experience = self._find_lines_with_keywords(
            resume_text,
            ["experience", "intern", "worked", "job", "company"],
        )

        return {
            "skills": skills,
            "education": education,
            "projects": projects,
            "experience": experience,
        }

    def _find_lines_with_keywords(self, text: str, keywords: list[str]) -> list[str]:
        """Find lines that contain at least one keyword."""
        matching_lines = []

        for line in text.splitlines():
            clean_line = line.strip()

            # Skip empty lines so the output stays neat.
            if not clean_line:
                continue

            # Skip simple section headings such as "Projects:".
            if clean_line.endswith(":"):
                continue

            lower_line = clean_line.lower()
            if any(keyword in lower_line for keyword in keywords):
                matching_lines.append(clean_line)

        return matching_lines
