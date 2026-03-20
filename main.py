import pytesseract
from pytesseract import Output
from PIL import Image, ImageFilter, ImageEnhance
import os
import sys
import argparse

# --- Set Tesseract path for Windows (edit if needed) ---
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp', '.webp'}

def validate_image_path(image_path):
    """Check file exists and has a supported format."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    ext = os.path.splitext(image_path)[1].lower()
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format '{ext}'. Supported: {SUPPORTED_FORMATS}")

def preprocess_image(img):
    """Enhance image for better OCR accuracy."""
    img = img.convert('L')                                      # Grayscale
    img = img.filter(ImageFilter.SHARPEN)                       # Sharpen edges
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)                                 # Boost contrast
    return img

def extract_text(image_path, lang='eng', preprocess=True):
    """Extract text from image with optional preprocessing."""
    validate_image_path(image_path)

    with Image.open(image_path) as img:
        if preprocess:
            img = preprocess_image(img)

        # Custom config: treat image as a single block of text
        config = '--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, lang=lang, config=config)

        # Get confidence score
        data = pytesseract.image_to_data(img, lang=lang, output_type=Output.DICT)
        confidences = [int(c) for c in data['conf'] if str(c).isdigit() and int(c) > 0]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0

        return text.strip(), avg_confidence

def save_output(text, image_path):
    """Save extracted text to a .txt file beside the image."""
    base = os.path.splitext(image_path)[0]
    output_path = f"{base}_extracted.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='OCR Image to Text Extractor')
    parser.add_argument('image', nargs='?', help='Path to image file')
    parser.add_argument('--lang', default='eng', help='Tesseract language code (default: eng)')
    parser.add_argument('--no-preprocess', action='store_true', help='Skip image preprocessing')
    parser.add_argument('--save', action='store_true', help='Save output to a .txt file')
    args = parser.parse_args()

    image_path = args.image or input("Enter the path to the image file: ").strip()

    try:
        print(f"\nProcessing: {image_path}")
        text, confidence = extract_text(
            image_path,
            lang=args.lang,
            preprocess=not args.no_preprocess
        )

        if not text:
            print("No text could be extracted from the image.")
            return

        print(f"Confidence Score: {confidence:.1f}%")
        print(f"\n--- Extracted Text ---\n{text}\n----------------------")

        if args.save:
            out = save_output(text, image_path)
            print(f"Text saved to: {out}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except pytesseract.TesseractNotFoundError:
        print("Tesseract is not installed or not found in PATH.")
        print("Install it from: https://github.com/UB-Mannheim/tesseract/wiki")
        sys.exit(1)

if __name__ == "__main__":
    main()