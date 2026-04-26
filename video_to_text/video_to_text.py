import cv2
import pytesseract

#Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Video path
video_path = "SAMPLE_VIDEOC.mp4"

# Open the  video
capture = cv2.VideoCapture(video_path)

# Check if video opened
if not capture.isOpened():
    print("Error: Cannot open video")
    exit()

frame_count = 0
all_text = []

print("Processing video...")

while True:
    ret, frame = capture.read()

    if not ret:
        break

    # Process every 30th frame
    if frame_count % 30 == 0:
        print(f"Reading frame {frame_count}")

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply threshold (improves OCR)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Extract text
        text = pytesseract.image_to_string(thresh)

        # Store text
        all_text.append(f"\n--- Frame {frame_count} ---\n{text}")

    frame_count += 1

# Release video
capture.release()
cv2.destroyAllWindows()

# Save output
with open("video_text_output.txt", "w", encoding="utf-8") as f:
    f.write("".join(all_text))

print("Done! Text saved in video_text_output.txt")

