import argparse
import pytesseract
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description='Extract text from an image using Tesseract OCR')
    parser.add_argument('png', help='Path to the PNG-file to be processed')
    parser.add_argument('txt', help='Path to the extracted text file')
    return parser.parse_args()


if __name__ == '__main__':
    # Read the arguments from the command line
    args = parse_args()
    print(args)
    # Read image
    image = Image.open(args.png)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Write the extracted text to file
    with open(args.txt, 'w') as f:
        f.write(text)
