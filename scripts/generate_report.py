"""
Generate a simple PDF report for the repository. Requires `reportlab`.
Run: python scripts/generate_report.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_report(output_path="docs/report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 80, "Hiring Assistant Chatbot - Project Report")

    c.setFont("Helvetica", 11)
    text_lines = [
        "Overview:",
        "This project implements a Hiring Assistant chatbot using Streamlit.",
        "",
        "Components:",
        "- Streamlit UI (app.py)",
        "- Chatbot logic (chatbot.py, prompts.py)",
        "- Utils (validators, question generator, context manager)",
        "- Data handler (simulated storage)",
        "",
        "How to run:",
        "1. pip install -r requirements.txt",
        "2. streamlit run app.py",
        "",
        "This PDF was generated using reportlab.",
    ]

    y = height - 120
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 16
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print(f"Report generated at {output_path}")

if __name__ == "__main__":
    generate_report()
