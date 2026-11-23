from pathlib import Path
import pytest
from utils.resume_parser import parse_resume

def test_parse_txt(tmp_path):
    file_path = tmp_path / "resume.txt"
    file_path.write_text("Python and SQL", encoding="utf-8")
    assert "Python" in parse_resume(str(file_path))

def test_reject_unsupported_file(tmp_path):
    file_path = tmp_path / "resume.csv"
    file_path.write_text("a,b", encoding="utf-8")
    with pytest.raises(ValueError):
        parse_resume(str(file_path))
