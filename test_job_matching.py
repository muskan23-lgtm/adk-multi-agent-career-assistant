from utils.ats_scorer import score_resume_job

def test_matching_detects_skills_and_gaps():
    resume = "Python SQL Pandas Excel"
    job = "Python SQL Pandas Excel Power BI Statistics"
    result = score_resume_job(resume, job)
    assert "Python" in result["matched_skills"]
    assert "Power BI" in result["not_demonstrated_skills"]
    assert 0 <= result["score"] <= 100

def test_empty_inputs_return_valid_score():
    result = score_resume_job("", "")
    assert result["score"] == 0
