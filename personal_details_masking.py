import re
import spacy
import pdfplumber
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def mask_personal_details(input_pdf, output_pdf):
    # Load the spaCy NER model
    nlp = spacy.load("en_core_web_lg")

    pdf = pdfplumber.open(input_pdf)

    c = canvas.Canvas(output_pdf, pagesize=letter)

    for page in pdf.pages:
        text = page.extract_text()

        # Apply NER to identify personal details
        doc = nlp(text)
        labels_to_filter = ["PERSON", "AGE", "GPE", "DATE"]
        entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ent.label_ in labels_to_filter]



        # Replace identified personal details with asterisks
        masked_text = text
        for start, end, label in entities:
            masked_text = masked_text[:start] + "*" * (end - start) + masked_text[end:]

        # Split the masked text into paragraphs
        paragraphs = re.split(r'\n\n', masked_text)

        # Set the font size and line height
        font_size = 10
        line_height = 1.5 * font_size

        # Set the starting position
        x = 35
        y = 500

        # Draw each paragraph of the masked text
        for paragraph in paragraphs:
            lines = paragraph.split("\n")

            for line in lines:
                c.setFont("Helvetica", font_size)
                c.drawString(x, y, line)
                y -= line_height

            # Add spacing between paragraphs
            y -= line_height

        c.showPage()

    pdf.close()
    c.save()




# Usage example
input_pdf = 'C:\\Users\\Harish Reddy\\Downloads\\sample-pdf-with-images.pdf'
output_pdf = 'C:\\Users\\Harish Reddy\\Downloads\\output.pdf'

mask_personal_details(input_pdf, output_pdf)




