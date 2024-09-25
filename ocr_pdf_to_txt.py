import argparse
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description='Extract text from an image using Tesseract OCR')
    parser.add_argument('pdf', help='Path to the PDF-file to be processed')
    parser.add_argument('txt', help='Path to the extracted text file')
    return parser.parse_args()

args = parse_args()

# Convert PDF to images
pages = convert_from_path(args.pdf, 300)  # 300 DPI is recommended for good OCR quality

# Initialize text output
text = ""
# Iterate over all the pages
with open(args.txt, "w") as text_file:
    for page_number, page_data in enumerate(pages):
        print(f"Page {page_number+1:3d} of {len(pages)}")
        # Convert PIL image to a string
        page_text = pytesseract.image_to_string(page_data)
        text = f"--- Start of Page {page_number + 1} ---\n"
        text += page_text + "\n"
        text += f"--- End of Page {page_number + 1} ---\n"
        text_file.write(text)

print(f"Text extraction complete. Check '{args.txt}' for the result.")
