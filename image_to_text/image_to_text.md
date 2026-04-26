2.Program to scan a image PDF and extract the content:

 -This program extracts text from images using Optical Character Recogition(OCR).It uses Tesseract OCR with python to read and convert image text into machine readable format.

 -Requirements
 1.Python
 2.OpenCV
 3.OCR
 4.pytesseract

 1.OpenCV:OpenCV (Open Source Computer Vision Library) is a library use to work with images, videos and perform computer vision tasks.
 -Helps in image processing, video processing tasks and computer vision tasks.
 -Reads image and converts it to better format (grayscale).

 2.Pytesseract is a python library used to extract text from images, it is a OCR tool for python.

 3.OCR: OCR(Optical Character Recognition) is the procedure that transforms a image's into a text format that is readable and editable by machine.

 Real-word use-case:
 1.Invoice & billing processing helps in finance data migration.
 2.Healthcare: Scan patient reports and convert to digital records and helps to access data easily.
 3.Data entry automation: Instead of typing manually OCR extracts data automatically.

 Tested the program as follows:

-image_to_text.py - main program 
-sample_image1B.png - sample image with png extension(works well with .jpg or .jpeg files)
-command to run the program python3 image_to_text.py (make sure we are in correct directory)
-Output will be displayed in the terminal itself

Installing dependencies:

-Install tesseract: Download and install from tesseract OCR from official source: https://github.com/madmaze/pytesseract
then run 
pip install pytesseract
-Install openCV :
open command prompt and run 
pip install opencv-python





