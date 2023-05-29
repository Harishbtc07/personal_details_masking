import spacy
import fitz

# Load spaCy model
nlp = spacy.load('en_core_web_lg')

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

masked_text = ""
for token in doc:
    if token.ent_type_ in ['PERSON', 'DATE', 'GPE', 'AGE', 'ADDRESS']:
        masked_text += '[******]'
    else:
        masked_text += token.text_with_ws

# Function to save masked text as PDF
def save_text_as_pdf(text, output_pdf_path):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text(fitz.Point(50, 50), text)
    doc.save(output_pdf_path)

# Path to save the masked PDF
output_pdf_path = 'C:\\Users\\Harish Reddy\\Downloads\\masked_output.pdf'

# Save masked text as PDF
save_text_as_pdf(masked_text, output_pdf_path)
