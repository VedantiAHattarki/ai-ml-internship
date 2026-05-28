# AI-ML Internship Project

## OCR File Processing and Automation System

This project is an end-to-end **OCR (Optical Character Recognition) File Processing and Automation System** developed as part of my AI/ML internship work.

The main goal of this project is to extract text from different types of files such as **PDFs, images, and videos** using OCR techniques. The project was initially developed as separate Python programs and later upgraded into a structured **FastAPI-based Python package** with Swagger UI support.

The system currently supports:

* Image to text extraction
* PDF to text extraction
* Video to text extraction
* API testing using Swagger UI
* Virtual environment-based dependency management
* AWS S3-based file processing workflow
* Scheduler-based automation
* File classification for routing files to the correct OCR service

---

## Overview

In the earlier version, the OCR programs were written separately for images, PDFs, and videos. Later, these programs were arranged into a proper Python package structure and exposed as REST APIs using FastAPI.

FastAPI provides automatic API documentation through Swagger UI, which allows the APIs to be tested directly from the browser without using Postman.

This project simulates a real-world backend automation system where files can be uploaded, processed, classified, and stored in an organized way.

---

## Completed Work Till Date

### 1. FastAPI Package Structure

The separate OCR programs were merged into a single modular Python package.

The project is now organized into:

* `api` layer for FastAPI route files
* `services` layer for OCR processing logic
* `utils` layer for helper functions
* `core` layer for configuration files

This makes the project easier to understand, maintain, and extend.

---

### 2. FastAPI APIs and Swagger UI

The OCR functionalities are exposed using FastAPI APIs.

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

Current API endpoints:

```text
GET  /api/health
POST /api/image/process
POST /api/pdf/process
POST /api/video/process
```

All image, PDF, and video APIs were tested successfully using Swagger UI.

---

### 3. Image OCR

The image OCR service extracts text from image files such as JPG, JPEG, and PNG.

The image processing flow includes:

* Reading the uploaded image
* Converting the image to grayscale
* Resizing the image for better OCR accuracy
* Applying Gaussian blur
* Applying adaptive thresholding
* Extracting text using PyTesseract OCR
* Returning the extracted text through the API response

---

### 4. PDF OCR

The PDF OCR service supports both digital PDFs and scanned PDFs.

For digital PDFs:

* PyMuPDF is used to extract text directly from the PDF.

For scanned PDFs:

* PDF2Image converts PDF pages into images.
* OpenCV preprocesses the image pages.
* PyTesseract extracts text from each page.

This allows the system to handle both text-based and image-based PDF files.

---

### 5. Video OCR

The video OCR service extracts visible text from video frames.

The video processing flow includes:

* Reading the uploaded video using OpenCV
* Selecting frames at fixed intervals
* Preprocessing each selected frame
* Extracting text using PyTesseract
* Removing duplicate and noisy text
* Returning the final cleaned text

This helps reduce repeated text and improves the readability of video OCR output.

---

### 6. Virtual Environment Support

A virtual environment is used to manage all Python dependencies.

The `.venv/` folder is used locally and is not pushed to GitHub.

All required packages are stored in:

```text
requirements.txt
```

This allows the project to be set up easily on another system using:

```bash
python -m pip install -r requirements.txt
```

---

### 7. AWS S3 and Scheduler Support

The project also includes AWS S3-based automation.

The scheduler monitors the S3 input folder. When a new file is found, it downloads the file, classifies it, processes it using the correct OCR service, uploads the output text file to S3, and moves the original file to the processed folder.

S3 workflow:

```text
File uploaded to input/
        ↓
Scheduler detects the file
        ↓
Classifier identifies the file type
        ↓
Correct OCR service is called
        ↓
Extracted text is generated
        ↓
Output file is uploaded to output/
        ↓
Original file is moved to processed/
```

S3 folder structure:

```text
ai-ml-project-bucket/
│
├── input/
├── output/
└── processed/
```

---

## Project Structure

```text
ai-ml-internship/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_health.py
│   │   ├── routes_image.py
│   │   ├── routes_pdf.py
│   │   └── routes_video.py
│
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│
│   ├── services/
│   │   ├── __init__.py
│   │   ├── image_service.py
│   │   ├── pdf_service.py
│   │   ├── video_service.py
│   │   ├── classifier_service.py
│   │   └── s3_service.py
│
│   └── utils/
│       ├── __init__.py
│       └── file_utils.py
│
├── old_code/
│   └── previous Flask and standalone OCR files
│
├── sample_files/
│   ├── images/
│   ├── pdfs/
│   └── videos/
│
├── screenshots/
├── temp/
├── tests/
│
├── scheduler.py
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* FastAPI
* Swagger UI
* Uvicorn
* OpenCV
* PyTesseract OCR
* PyMuPDF
* PDF2Image
* NumPy
* Pillow
* AWS S3
* Boto3
* Python Dotenv
* Schedule

---

## FastAPI Workflow

```text
User uploads a file through Swagger UI
        ↓
FastAPI route receives the uploaded file
        ↓
File is saved temporarily in temp/
        ↓
Related OCR service function is called
        ↓
OCR processing is performed
        ↓
Extracted text is returned as JSON response
```

Example API response:

```json
{
  "status": "success",
  "filename": "sample.pdf",
  "file_type": "pdf",
  "extracted_text": "Extracted text appears here"
}
```

---



## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/VedantiAHattarki/ai-ml-internship.git
cd ai-ml-internship
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

---

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 5. Run the FastAPI Application

```bash
python run.py
```

If the application starts successfully, the terminal will show:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

### 6. Open Swagger UI

Open this URL in the browser:

```text
http://127.0.0.1:8000/docs
```

---

## Testing APIs in Swagger UI

1. Open Swagger UI.
2. Select the API endpoint.
3. Click `Try it out`.
4. Upload a file if the endpoint requires it.
5. Click `Execute`.
6. Check the response body.

This allows the image, PDF, and video APIs to be tested directly from the browser.

---

## Running the Scheduler

The scheduler is used for AWS S3 automation.

Run:

```bash
python scheduler.py
```

The scheduler monitors the S3 input folder and automatically processes new files.

---

## Environment Variables

The project uses a `.env` file for configuration.

Example `.env` file:

```env
AWS_REGION=ap-south-1
INPUT_BUCKET=ai-ml-project-bucket
OUTPUT_BUCKET=ai-ml-project-bucket
INPUT_PREFIX=input/
OUTPUT_PREFIX=output/
PROCESSED_PREFIX=processed/
TEMP_FOLDER=temp
```

If AWS credentials are needed locally:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

The `.env` file should not be pushed to GitHub.

---

## Classifier Logic

The classifier identifies the uploaded file type based on its extension and PDF content.

It supports:

* Digital PDF
* Scanned PDF
* Image
* Video
* Unknown file type

Based on the classification result, the file is routed to the correct OCR service.

---

## Output

The extracted text is returned through the API response.

For S3 automation, the extracted text is saved as a `.txt` file and uploaded to the S3 `output/` folder.

---

## Screenshots

###  API Testing (Postman)

### process-pdf

![Postman](screenshots/postman_pdf_preview.png)

### process-image

![Postman](screenshots/postman_image_preview.png)

### process-video

![Postman](screenshots/postman_video_preview.png)

###  AWS S3 Input

![S3 Input](screenshots/s3_input.png)

###  AWS S3 Output

![S3 Output](screenshots/s3_output.png)

###  Scheduler Execution

![Scheduler](screenshots/scheduler.png)

### AWS S3 Processed

![S3 Processed](screenshots/s3_processed.png)

### FastAPI Swagger UI
![FastAPI Swagger UI](screenshots/FastAPI_Swagger_UI.jpeg)



---

## Current Status

Completed:

* Converted old OCR programs into a modular FastAPI package
* Added API routes for image, PDF, and video processing
* Added a health check API
* Added Swagger UI support
* Tested image, PDF, and video APIs successfully through Swagger UI
* Added virtual environment support
* Updated `requirements.txt`
* Added `.gitignore`
* Organized old files under `old_code`
* Added S3 scheduler support using the new package structure

---

## Limitations

* OCR accuracy depends on the quality of the input file
* Low-resolution images may produce incorrect text
* Video OCR may take more time for longer videos
* Some extracted text may contain spelling or formatting errors
* Scanned PDF processing requires Tesseract and Poppler setup

---

## Future Enhancements

* Add Pytest unit tests
* Generate test coverage report using pytest-cov
* Add benchmarking using pytest-benchmark and timeit
* Add GitHub Actions for automatic build and testing
* Deploy the application using AWS App Runner
* Create AWS CloudFormation templates
* Improve OCR accuracy using better preprocessing
* Add a simple Streamlit frontend
* Explore EasyOCR or AWS Textract for improved OCR accuracy

---

## Learning Outcome

Through this project, I learned how to convert separate Python OCR scripts into a structured backend application. I also learned how to organize code into a package structure, expose OCR functions through FastAPI APIs, test APIs using Swagger UI, manage dependencies using a virtual environment, and connect the workflow with AWS S3 automation.

This project helped me understand how a backend OCR processing system can be designed in a more organized, reusable, and industry-oriented way.

---

## Author

**Vedanti Hattarki**
