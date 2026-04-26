import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Convert PDF to images
images = convert_from_path(
    "Task1A.pdf",
    poppler_path=r"C:\Users\hatta\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"
)

 # Opens a text file to save output in sample_output.txt
with open("sample_output.txt", "w", encoding="utf-8") as file:

    for i, img in enumerate(images):
        print(f"Processing page {i+1}...")

        # Extract text using OCR
        text = pytesseract.image_to_string(img)

        # Simple cleaning
        text = text.replace("-\n", "")

        # Write to file
        file.write(f"\n--- Page {i+1} ---\n")
        file.write(text)

print("Done! Text saved in sample_output.txt")