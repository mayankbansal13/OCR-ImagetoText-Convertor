🔍 OCR Image to Text Extractor
A command-line tool to extract text from images using Tesseract OCR and Python. Supports preprocessing for better accuracy, confidence scoring, multi-language extraction, and optional file output.

✨ Features

🖼️ Image to text extraction — powered by Tesseract OCR engine
🎨 Auto image preprocessing — grayscale, contrast boost, sharpening for better accuracy
📊 Confidence scoring — shows how reliable the extracted text is
🌍 Multi-language support — works with 100+ languages Tesseract supports
💾 Save to file — optionally export extracted text as a .txt file
✅ Format validation — catches unsupported file types early
🖥️ CLI interface — clean argument-based usage with argparse


🖥️ Demo
bash$ python ocr.py invoice.png --save

Processing: invoice.png
Confidence Score: 91.3%

--- Extracted Text ---
Invoice #4521
Date: March 15, 2024
Total Amount: $1,250.00
----------------------

Text saved to: invoice_extracted.txt

📦 Requirements

Python 3.7+
pytesseract
Pillow
Tesseract OCR (system install — see below)


🚀 Getting Started
Step 1 — Install Tesseract OCR (system dependency)
Tesseract must be installed at the OS level before anything else.
Windows:
Download and run the installer from UB-Mannheim
macOS:
bashbrew install tesseract
Ubuntu / Debian:
bashsudo apt install tesseract-ocr

Step 2 — Windows only: set Tesseract path
Uncomment this line in ocr.py:
pythonpytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
macOS and Linux users can skip this — Tesseract is auto-detected from PATH.

Step 3 — Install Python dependencies
bashpip install -r requirements.txt

Step 4 — Run the tool
bashpython ocr.py image.png

🛠️ Usage
bashpython ocr.py [image] [options]
Arguments
ArgumentDescriptionimagePath to the image file (optional — will prompt if not provided)--langTesseract language code (default: eng)--no-preprocessSkip image preprocessing--saveSave extracted text to a .txt file
Examples
bash# Basic extraction
python ocr.py photo.png

# Save output to file
python ocr.py photo.png --save

# Extract Hindi text
python ocr.py document.jpg --lang hin

# Skip preprocessing (for already clean images)
python ocr.py scan.tiff --no-preprocess

# Combine flags
python ocr.py receipt.jpg --lang eng --save

🌍 Language Support
Pass any valid Tesseract language code with --lang:
LanguageCodeEnglishengHindihinFrenchfraGermandeuSpanishspaChinese (Simplified)chi_simArabicara
To install additional languages:
Ubuntu:
bashsudo apt install tesseract-ocr-hin   # example: Hindi
macOS:
bashbrew install tesseract-lang
Full list of language codes: Tesseract Language List

🖼️ Supported Image Formats
FormatExtensionPNG.pngJPEG.jpg, .jpegTIFF.tiff, .tifBitmap.bmpWebP.webp

📁 Project Structure
ocr-extractor/
├── ocr.py               # Main script
├── requirements.txt     # Python dependencies
└── README.md            # This file
Output files (when using --save) are saved in the same folder as the input image:
invoice.png  →  invoice_extracted.txt

⚙️ How Preprocessing Works
When preprocessing is enabled (default), the image goes through:

Grayscale conversion — removes color noise
Sharpening — enhances text edges
Contrast boost (2×) — makes text stand out from background

This significantly improves accuracy on photos, scans, and screenshots. Use --no-preprocess only if your image is already a clean, high-resolution scan.

📊 Confidence Score
After extraction, a confidence score (0–100%) is shown:
ScoreMeaning90–100%Excellent — clean image, clear text70–89%Good — minor noise or blur50–69%Fair — consider preprocessing or better imageBelow 50%Poor — image quality likely needs improvement

🛠️ Troubleshooting
TesseractNotFoundError
→ Tesseract is not installed or not in PATH. Follow Step 1 above.
Windows: Tesseract found but still errors
→ Uncomment and set the path in ocr.py (Step 2).
Low confidence / garbled output
→ Try with a higher resolution image. Avoid --no-preprocess unless the image is already clean.
UnsupportedFormat error
→ Convert your image to PNG or JPEG first using any image editor.
Language not found
→ Install the language pack for your OS (see Language Support section above).

📄 License
MIT License — free to use, modify, and distribute.

🙌 Acknowledgements

Tesseract OCR — open-source OCR engine by Google
pytesseract — Python wrapper for Tesseract
Pillow — image processing library