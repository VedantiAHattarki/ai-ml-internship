import cv2
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image using OpenCV
img = cv2.imread("sample_image1B.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold (improves OCR accuracy)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Extract text
text = pytesseract.image_to_string(thresh)

# Clean output
print(text.replace("\x0c", "").strip())