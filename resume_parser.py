"""Extract text from PDF, DOCX and TXT resumes."""

from pathlib import Path

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}

def parse_resume(file_path: str) -> str:
    path = Path(file_path)
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {suffix}. Use PDF, DOCX or TXT.")

    if suffix == ".txt":
        return path.read_text(encoding="utf-8", errors="ignore")

    if suffix == ".pdf":
        import fitz
        with fitz.open(path) as document:
            return "\n".join(page.get_text("text") for page in document)

    from docx import Document
    document = Document(path)
    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
    for table in document.tables:
        for row in table.rows:
            paragraphs.append(" | ".join(cell.text for cell in row.cells))
    return "\n".join(paragraphs)
