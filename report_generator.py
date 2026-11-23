"""Generate a compact downloadable PDF career analysis report."""

from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf_report(result: dict, role_title: str = "Target role") -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Career Fit Analysis Report", styles["Title"]),
        Paragraph(f"Target role: {role_title}", styles["Heading2"]),
        Spacer(1, 12),
        Paragraph(f"Estimated match score: {result['score']}%", styles["Heading1"]),
        Paragraph(result["note"], styles["Italic"]),
        Spacer(1, 12),
        Paragraph("Score breakdown", styles["Heading2"]),
    ]
    data = [["Metric", "Coverage"], ["Skill coverage", f"{result['skill_coverage']}%"],
            ["Keyword coverage", f"{result['keyword_coverage']}%"],
            ["Experience/education signals", f"{result['experience_signal_coverage']}%"]]
    table = Table(data, colWidths=[300, 130])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#243B53")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("PADDING", (0,0), (-1,-1), 7),
    ]))
    story.extend([table, Spacer(1, 14), Paragraph("Matched skills", styles["Heading2"])])
    story.append(Paragraph(", ".join(result["matched_skills"]) or "None detected", styles["BodyText"]))
    story.extend([Spacer(1, 10), Paragraph("Skills not demonstrated", styles["Heading2"])])
    story.append(Paragraph(", ".join(result["not_demonstrated_skills"]) or "No gaps detected in the current taxonomy", styles["BodyText"]))
    story.extend([Spacer(1, 10), Paragraph("Matched keywords", styles["Heading2"])])
    story.append(Paragraph(", ".join(result["matched_keywords"][:50]) or "None detected", styles["BodyText"]))
    doc.build(story)
    return buffer.getvalue()
