"""Coordinator Agent for running all career assistant agents."""

from agents.job_match_agent import JobMatchingAgent
from agents.resume_agent import ResumeAgent
from agents.skill_gap_agent import SkillGapAgent


class CoordinatorAgent:
    """Coordinate resume analysis, job matching, and skill gap analysis."""

    def __init__(self) -> None:
        """Create all sub-agents used by the coordinator."""
        self.resume_agent = ResumeAgent()
        self.job_matching_agent = JobMatchingAgent()
        self.skill_gap_agent = SkillGapAgent()

    def create_recommendation(
        self,
        resume_text: str,
        job_description_text: str,
    ) -> str:
        """Run all agents and return one final recommendation report."""
        resume_info = self.resume_agent.extract_information(resume_text)
        job_match_info = self.job_matching_agent.compare(
            resume_info=resume_info,
            job_description_text=job_description_text,
        )
        skill_gap_info = self.skill_gap_agent.find_gaps(
            resume_info=resume_info,
            job_match_info=job_match_info,
        )

        return self._format_report(
            resume_info=resume_info,
            job_match_info=job_match_info,
            skill_gap_info=skill_gap_info,
        )

    def _format_report(
        self,
        resume_info: dict,
        job_match_info: dict,
        skill_gap_info: dict,
    ) -> str:
        """Format all agent outputs into a readable report."""
        match_score = job_match_info["match_score"]
        final_advice = self._get_final_advice(match_score)

        report = [
            "AI Career Assistant Recommendation",
            "=" * 38,
            "",
            "Resume Agent Output",
            "-" * 19,
            f"Skills found: {self._format_list(resume_info['skills'])}",
            f"Education found: {self._format_list(resume_info['education'])}",
            f"Projects found: {self._format_list(resume_info['projects'])}",
            f"Experience found: {self._format_list(resume_info['experience'])}",
            "",
            "Job Matching Agent Output",
            "-" * 25,
            f"Job skills found: {self._format_list(job_match_info['job_skills'])}",
            f"Matching skills: {self._format_list(job_match_info['matching_skills'])}",
            f"Match score: {match_score}%",
            "",
            "Skill Gap Agent Output",
            "-" * 22,
            f"Missing skills: {self._format_list(skill_gap_info['missing_skills'])}",
            "Learning plan:",
            self._format_bullets(skill_gap_info["learning_plan"]),
            "",
            "Final Recommendation",
            "-" * 20,
            final_advice,
        ]

        return "\n".join(report)

    def _get_final_advice(self, match_score: int) -> str:
        """Choose a simple final recommendation based on the match score."""
        if match_score >= 75:
            return "You are a strong match. Apply now and tailor your resume keywords."

        if match_score >= 50:
            return "You are a fair match. Apply, but improve the missing skills soon."

        return "Build the missing skills first, then apply with stronger projects."

    def _format_list(self, values: list[str]) -> str:
        """Return a friendly string for a list of values."""
        if not values:
            return "None found"

        return ", ".join(values)

    def _format_bullets(self, values: list[str]) -> str:
        """Return a simple bullet list as text."""
        if not values:
            return "- No major skill gaps found."

        return "\n".join(f"- {value}" for value in values)

