
import spacy
import fitz

# Load spaCy model
from PyPDF2 import PdfReader

nlp = spacy.load('en_core_web_lg')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text


# Function to mask personal details in text
def mask_text(doc):
    masked_text = ""
    for token in doc:
        if token.ent_type_ in ['PERSON', 'DATE', 'ADDRESS', 'GPE', 'AGE', 'DOB', 'PHONE', 'LOC', 'MONEY']:
            masked_text += '[******]'
        else:
            masked_text += token.text_with_ws
    return masked_text


# Function to save masked text as PDF
def save_text_as_pdf(text, input_pdf_path, output_pdf_path, annotation_color=(0, 1, 0)):
    pdf = PdfReader(input_pdf_path)
    total_pages = len(pdf.pages)

    doc = fitz.open(input_pdf_path)
    for page_number in range(total_pages):
        page = doc.load_page(page_number)
        words = page.get_text("words")

        for word in words:
            if word[4] == text:
                bbox = fitz.Rect(word["x0"], word["y0"], word["x1"], word["y1"])
                page.add_rect_annot(bbox, fill_color=annotation_color)

        page.apply_redactions()

    doc.save(output_pdf_path)

# Path to the input PDF
pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\Sample Patient Profiles and Prescriptions.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Apply NER and mask personal details in text
doc = nlp(pdf_text)
masked_text = mask_text(doc)

# Path to save the masked PDF
output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\output.pdf'

# Save masked text as PDF
save_text_as_pdf(masked_text, pdf_path, output_pdf_path)
