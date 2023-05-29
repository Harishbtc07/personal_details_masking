# import spacy
# import fitz
#
# # Load spaCy model
# nlp = spacy.load('en_core_web_lg')
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text = ""
#     for page in document:
#         text += page.get_text()
#     return text
#
# # Path to the input PDF
# pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\HK_resume.pdf'
#
# # Extract text from PDF
# pdf_text = extract_text_from_pdf(pdf_path)
#
# # Apply NER and mask personal details
# doc = nlp(pdf_text)
#
# masked_text = ""
# for token in doc:
#     if token.ent_type_ in ['PERSON', 'DATE', 'ADDRESS']:
#         masked_text += '[REDACTED]'
#     else:
#         masked_text += token.text_with_ws
#
#
# # Function to save masked text as PDF
# def save_text_as_pdf(text, input_pdf_path, output_pdf_path):
#     doc = fitz.open(input_pdf_path)
#     for page in doc:
#         page_text = page.get_text("text")
#         page_text = page_text.replace("\n", " ")
#         for token in nlp(page_text).ents:
#             if token.label_ in ['PERSON', 'DATE', 'ADDRESS']:
#                 mask_text = '[******]'
#                 bbox = page.search_for(token.text, hit_max=1)[0]
#                 rect = fitz.Rect(bbox.x0, bbox.y0, bbox.x1, bbox.y1)
#                 page.insert_textbox(rect, mask_text, fontsize=8, fill=(0, 0, 0), rotate=0)
#     doc.save(output_pdf_path)
#
#
#
# # Path to save the masked PDF
# output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\masked_output.pdf'
#
# # Save masked text as PDF
# save_text_as_pdf(masked_text, pdf_path, output_pdf_path)

#
#
#
#
#
#
# import spacy
# import fitz
#
# # Load spaCy model
# nlp = spacy.load('en_core_web_sm')
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text = ""
#     for page in document:
#         text += page.get_text()
#     return text
#
# # Path to the input PDF
# pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\sample.pdf'
#
# # Extract text from PDF
# pdf_text = extract_text_from_pdf(pdf_path)
#
# # Apply NER and mask personal details
# doc = nlp(pdf_text)
#
# masked_text = ""
# for token in doc:
#     if token.ent_type_ in ['PERSON', 'DATE', 'ADDRESS','AGE']:
#         masked_text += '[REDACTED]'
#     else:
#         masked_text += token.text_with_ws
#
# # Function to save masked text as PDF
# def save_text_as_pdf(text, input_pdf_path, output_pdf_path):
#     doc = fitz.open(input_pdf_path)
#     for page in doc:
#         page_text = page.get_text("text")
#         page_text = page_text.replace("\n", " ")
#         doc_page = nlp(page_text)
#
#
#     doc.save(output_pdf_path)
#
# # Path to save the masked PDF
# output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\masked_output.pdf'
#
# # Save masked text as PDF
# save_text_as_pdf(masked_text, pdf_path, output_pdf_path)





# import spacy
# import fitz
#
# # Load spaCy model
# nlp = spacy.load('en_core_web_lg')
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text = ""
#     for page in document:
#         text += page.get_text() + "\n\n\n"  # Add two newlines between paragraphs
#     return text
#
# # Path to the input PDF
# input_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\sample.pdf'
#
# # Extract text from PDF
# pdf_text = extract_text_from_pdf(input_pdf_path)
#
# # Apply NER and mask personal details
# doc = nlp(pdf_text)
#
# masked_text = ""
# for token in doc:
#     if token.ent_type_ in ['PERSON', 'DATE', 'GPE', 'AGE']:
#         masked_text += '[******]'
#     else:
#         masked_text += token.text_with_ws
#
# # Function to save masked text as PDF
# def save_text_as_pdf(text, output_pdf_path):
#     doc = fitz.open()
#     page = doc.new_page()
#     page.insert_text(fitz.Point(50, 50), text)
#     doc.save(output_pdf_path)
#
# # Path to save the masked PDF
# output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\masked_output.pdf'
#
# # Save masked text as PDF
# save_text_as_pdf(masked_text, output_pdf_path)
#

# import re
# import spacy
# import pdfplumber
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
# def mask_personal_details(input_pdf, output_pdf):
#     # Load the spaCy NER model
#     nlp = spacy.load("en_core_web_lg")
#
#     pdf = pdfplumber.open(input_pdf)
#
#     c = canvas.Canvas(output_pdf, pagesize=letter)
#
#     for page in pdf.pages:
#         text = page.extract_text()
#
#         # Apply NER to identify personal details
#         doc = nlp(text)
#         labels_to_filter = ["PERSON", "AGE", "GPE", "DATE"]
#         entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ent.label_ in labels_to_filter]
#
#
#
#         # Replace identified personal details with asterisks
#         masked_text = text
#         for start, end, label in entities:
#             masked_text = masked_text[:start] + "*" * (end - start) + masked_text[end:]
#
#         # Split the masked text into paragraphs
#         paragraphs = re.split(r'\n\n', masked_text)
#
#         # Set the font size and line height
#         font_size = 12
#         line_height = 1.5 * font_size
#
#         # Set the starting position
#         x = 100
#         y = 700
#
#         # Draw each paragraph of the masked text
#         for paragraph in paragraphs:
#             lines = paragraph.split("\n")
#
#             for line in lines:
#                 c.setFont("Helvetica", font_size)
#                 c.drawString(x, y, line)
#                 y -= line_height
#
#             # Add spacing between paragraphs
#             y -= line_height
#
#         c.showPage()
#
#     pdf.close()
#     c.save()
#
#
#
#
# # Usage example
# input_pdf = 'C:\\Users\\Harish Reddy\\Downloads\\sample.pdf'
# output_pdf = 'C:\\Users\\Harish Reddy\\Downloads\\masked_output.pdf'
#
# mask_personal_details(input_pdf, output_pdf)



# import re
# import spacy
# import fitz
#
# # Load spaCy model
# nlp = spacy.load('en_core_web_lg')
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text = ""
#     for page in document:
#         text += page.get_text() + "\n\n\n"  # Add two newlines between paragraphs
#     return text
#
# # Path to the input PDF
# input_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\sample-pdf-with-images.pdf'
#
# # Extract text from PDF
# pdf_text = extract_text_from_pdf(input_pdf_path)
#
# # Define regular expressions to match and mask personal details
# name_regex = re.compile(r'John Doe')
# date_regex = re.compile(r'\b\d{1,2}/\d{1,2}/\d{4}\b')
# address_regex = re.compile(r'123 Main St')
#
# # Mask personal details using regex
# masked_text = re.sub(name_regex, '[REDACTED]', pdf_text)
# masked_text = re.sub(date_regex, '[REDACTED]', masked_text)
# masked_text = re.sub(address_regex, '[REDACTED]', masked_text)
#
# # Function to save masked text as PDF
# def save_text_as_pdf(text, input_pdf_path, output_pdf_path):
#     doc = fitz.open(input_pdf_path)
#     for page in doc:
#         page_text = page.get_text("text")
#         page_text = page_text.replace("\n", " ")
#         doc_page = nlp(page_text)
#
#         for token in doc_page.ents:
#             if token.label_ in ['PERSON', 'DATE', 'GPE', 'ADDRESS']:
#                 mask_text = '[******]'
#                 bbox = page.search_for(token.text, hit_max=1)[0]
#                 rect = fitz.Rect(bbox.x0, bbox.y0, bbox.x1, bbox.y1)
#                 page.insert_textbox(rect, mask_text, fontsize=8, fill=(0, 0, 0), rotate=0)
#     doc.save(output_pdf_path)
#
# # Path to save the masked PDF
# output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\output.pdf'
#
# # Save masked text as PDF
# save_text_as_pdf(masked_text, input_pdf_path, output_pdf_path)
import os

import spacy
import fitz
from PIL import Image

# Load spaCy model
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
        if token.ent_type_ in ['PERSON', 'DATE', 'ADDRESS']:
            masked_text += '[REDACTED]'
        else:
            masked_text += token.text_with_ws
    return masked_text

# Function to save masked text as PDF
def save_text_as_pdf(text, input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    for page in doc:
        page_text = page.get_text("text")
        page_text = page_text.replace("\n", " ")
        for token in nlp(page_text).ents:
            if token.label_ in ['PERSON', 'DATE', 'ADDRESS']:
                mask_text = '[******]'
                bbox = page.search_for(token.text, hit_max=1)[0]
                rect = fitz.Rect(bbox.x0, bbox.y0, bbox.x1, bbox.y1)
                page.insert_textbox(rect, mask_text, fontsize=8, fill=(0, 0, 0), rotate=0)
    doc.save(output_pdf_path)

# Function to mask images in PDF
def mask_images(pdf_path, output_pdf_path):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            image_extension = base_image["ext"]
            image_file = f"temp_image.{image_extension}"
            with open(image_file, "wb") as f:
                f.write(image_data)

            # Replace the image with a blank (black) image
            width = int(img["width"])
            height = int(img["height"])
            blank_image = Image.new("RGB", (width, height), color=(0, 0, 0))
            blank_image.save(image_file)

            rect = fitz.Rect(img["rect"])
            page.insert_image(rect, filename=image_file, overlay=True)

            # Remove the temporary image file
            os.remove(image_file)

    doc.save(output_pdf_path)

# Path to the input PDF
pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\HK_resume.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Apply NER and mask personal details in text
doc = nlp(pdf_text)
masked_text = mask_text(doc)

# Path to save the masked PDF
output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\resume_output.pdf'

# Save masked text as PDF
save_text_as_pdf(masked_text, pdf_path, output_pdf_path)

# Mask images in the PDF
mask_images(pdf_path, output_pdf_path)

