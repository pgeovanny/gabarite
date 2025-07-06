from flask import make_response
from models import Question
import pdfkit

def export_questions_pdf(user_id):
    # Query questions and render HTML, then convert
    html = '<h1>Exported Questions</h1>'  # Simplified
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=questions.pdf'
    return response