import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfReader, PdfWriter

def add_logo_to_pdf(pdf_file, output_pdf_path, logo):
    # Create a PDF canvas
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Draw the logo on the canvas
    logo_reader = ImageReader(logo)
    can.drawImage(logo_reader, 10, 10, width=590, height=120)

    # Close the canvas
    can.save()

    # Move the buffer position to the beginning
    packet.seek(0)
    
    # Create a new PDF with the logo
    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(pdf_file)
    output = PdfWriter()

    # Add the logo to each page of the existing PDF
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    # Write the result to the output PDF file
    with open(output_pdf_path, "wb") as outputStream:
        output.write(outputStream)
