from pypdf import PdfReader


# Get resume from pdf file
# TODO: add support for OCR to extract text from images
def get_resume_from_bytes_pdf(pdf_bytes):

    reader = PdfReader(pdf_bytes)
    
    resume = ""
    for page in reader.pages:
        resume += page.extract_text()

    return resume
    
