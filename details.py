import os

import spacy
import fitz
from PIL import Image

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text

# Path to the input PDF
pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\HK_resume.pdf'



# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Apply NER and mask personal details
doc = nlp(pdf_text)

# Function to mask personal details in text
def mask_text(doc):
    masked_text = ""
    for token in doc:
        if token.ent_type_ in ['PERSON', 'DATE', 'ADDRESS']:
            masked_text += '[******]'
        else:
            masked_text += token.text_with_ws
    return masked_text

# Function to save masked text as PDF
def save_text_as_pdf(text, input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    for page in doc:
        page_text = page.get_text("text")
        #page_text = page_text.replace("\n", " ")
        for token in nlp(page_text).ents:
            if token.label_ in ['PERSON', 'DATE', 'ADDRESS']:
                mask_text = '[******]'
                #bbox = page.search_for(token.text, hit_max=1)[0]
                #rect = fitz.Rect(bbox.x0, bbox.y0 - 2, bbox.x1, bbox.y1 + 2)
                #page.insert_textbox(rect, mask_text, fontsize=8, fill=(1, 1, 1), rotate=0)
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
            image_width = base_image["width"]
            image_height = base_image["height"]
            blank_image = Image.new("RGB", (image_width, image_height), color=(0, 0, 0))
            blank_image.save(image_file)

            # Create the rectangle using the image properties
            rect = fitz.Rect(0, 0, image_width, image_height)
            page.insert_image(rect, filename=image_file, overlay=True)

            # Remove the temporary image file
            os.remove(image_file)

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

# Mask images in the PDF
mask_images(pdf_path, output_pdf_path)


