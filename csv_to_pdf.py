import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def csv_to_pdf(csv_path, pdf_path, title):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Calculate page size based on the number of rows and columns
    col_count = len(df.columns)
    row_count = len(df)
    page_width = max(letter[0], col_count * 1.5 * inch)  # Column width of 1.5 inches
    page_height = max(letter[1], (row_count + 2) * 0.3 * inch)  # Row height of 0.3 inches, plus space for title and date

    page_size = (page_width, page_height)
    
    # Create the PDF document
    doc = SimpleDocTemplate(pdf_path, pagesize=page_size)
    elements = []

    # Add title
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    elements.append(Paragraph(title, title_style))

    # Add date
    date_style = styles['Normal']
    date_str = datetime.now().strftime("%Y-%m-%d")
    elements.append(Paragraph(f"Date: {date_str}", date_style))

    # Add space after title and date
    elements.append(Paragraph(" ", date_style))

    # Create table data
    table_data = [df.columns.tolist()] + df.values.tolist()

    # Create the table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Build the PDF
    doc.build(elements)

# Modify the csv_path, pdf_path, and title variables as needed
csv_files = ["file.csv"]
pdf_files = ["output.pdf"]
title = "My pdf file"

for csv_path, pdf_path in zip(csv_files, pdf_files):
    csv_to_pdf(csv_path, pdf_path, title)
