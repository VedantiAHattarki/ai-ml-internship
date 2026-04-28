1.Program to scan a digital PDF and extract the content:

-This program extracts text from a PDF file using pytesseract.

-Requirements:
1.Python
2.Pytesseract
3.pdf2image
4.Poppler

1.Python
    -Python is used to connect all the tools and automate the process.
    -This program converts:
    pdf -> image -> OCR -> Text File
    hence python helps to run these steps together.

2.Pytesseract
    -Pytesseract is an OCR tool for python, enables to convert images containing text into string format that can be processed further.
    -Pytesseract does not do OCR by itself, it connects python to tesseract.
    -Used to extract text from images.

3.OCR(Optical Character Recognition):
    -OCR is a technology that converts images of text to actual editable text(machine readable text).

4.Poppler
    -Poppler is a tool that helps to convert pdf to images to extract the content.
    -Used by libraries like pdf2image which coverts the scanned pdf to image so that OCR can process them easily.


Program to scan a digital pdf and extract content is helpful for the following :
-Now a days there are many PDFs which are in scanned documents or images of text which makes tedious to search, edit or copy the text directly, hence the program converts PDFs to editable text.
-Converts to editable text, searchable content, easy to store and process.

Real-world uses:
-Data entry automation: Extract data from invoices and forms, avoids manual typing.
-Data Migration: Move data from old systems(PDFs) to new systems.
-Search Analysis: Make documents searchable.

Tested the program using the following PDFs:
-Task1A.pdf - sample pdf 
 sample_output.txt - sample pdf's output

Installing dependencies :
-Install python (version 3.8 or above)
while installing tick "add python to PATH"
-Install libraries:
 pip install pytesseract pdf2image pillow (in terminal)
-Install tesseract: Download and install from tesseract OCR from official source: https://github.com/madmaze/pytesseract
then run 
pip install pytesseract