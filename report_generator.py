from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_report(file_path, transcript, score, label):

    c = canvas.Canvas(file_path, pagesize=letter)
    y = 750

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "VBCUA Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, str(datetime.datetime.now()))

    y -= 30
    c.drawString(50, y, f"Score: {score}")
    c.drawString(50, y, f"Result: {label}")

    y -= 40
    c.drawString(50, y, "Transcript:")

    y -= 20
    for line in transcript.split("."):
        c.drawString(60, y, line.strip())
        y -= 15
        if y < 50:
            c.showPage()
            y = 750

    c.save()