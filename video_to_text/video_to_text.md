3.Program to scan a video and extract the content:

This program reads a video file and extracts text from it using OCR.

-Requirements:
1.Python
2.OpenCV
3.Pytesseract

1.Python is used as a controller, runs the program, connects OpenCV and pytesseract and handles loops, conditions and file saving.

2.OpenCV is used to handle the video and frames, it opens the video file, reads it frame-by-frame, converts frames into images and preprocesses frames(grayscale).

3.Pytesseract is used to extract text from each frame , it uses tesseract OCR and takes frames, detects characters and converts them into text.

Real-world use-case:
-Surveillance & security systems continuosly records videos which has vehile number plates, text on signboards etc., it helps to extract this content.
-Online lectures & education:helps to extract text from classes or tutorials, helps to create notes.
-Medical field: helps to process & extracts the patients monitoring videos and extract names and details on screens.
-Social media: Extract captions or text from videos

Tested the program as follows:
-video_to_text.py - main program
-SAMPLE_VIDEOC - sample video for processing
-video_text_output.txt - output file

Installing dependencies:

-Install tesseract: Download and install from tesseract OCR from official source: https://github.com/madmaze/pytesseract
then run 
pip install pytesseract
-Install openCV :
open command prompt and run 
pip install opencv-python


