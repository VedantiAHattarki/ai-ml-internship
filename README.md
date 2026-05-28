# AI-ML Internship Project

## OCR File Processing and Automation System

This project is an end-to-end **OCR (Optical Character Recognition) automation system** built as part of my AI/ML internship work. The system processes **PDF files, image files, and video files** and extracts readable text from them.

The project was initially developed as separate OCR programs and Flask APIs. It has now been upgraded into a clean **FastAPI-based Python package** with a modular structure, Swagger UI support, virtual environment dependency management, and reusable service layers.

---

## Overview

The main purpose of this project is to automate text extraction from different file formats using OCR and backend APIs.

The system can process:

* Digital PDFs
* Scanned PDFs
* Images
* Videos

It also includes support for AWS S3-based automation, where files can be uploaded to an input folder, processed automatically, and moved to output and processed folders.

This project simulates a real-world backend workflow where files are uploaded, classified, processed, and stored in a structured way.

---

## Completed Work

### 1. FastAPI Package Structure

The OCR programs were merged into a single Python package instead of keeping them as separate files.

The project is now organized into:

* `api` layer for FastAPI routes
* `services` layer for OCR and processing logic
* `utils` layer for helper functions
* `core` layer for configuration

This makes the code cleaner, reusable, and easier to maintain.

---

### 2. FastAPI APIs with Swagger UI

The image, PDF, and video OCR functionalities are exposed as REST APIs using FastAPI.

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

Using Swagger UI, the APIs can be tested directly from the browser without using Postman.

Available APIs:

```text
GET  /api/health
POST /api/image/process
POST /api/pdf/process
POST /api/video/process
```

---

### 3. Virtual Environment Support

A virtual environment is used to manage all Python dependencies for the project.

This helps keep project dependencies separate from the global Python installation.

The dependency list is maintained in:

```text
requirements.txt
```

The `.venv/` folder is ignored using `.gitignore`, so only the dependency list is pushed to GitHub.

---

### 4. OCR Processing

The project supports OCR processing for multiple file types.

For images:

* OpenCV is used for preprocessing
* PyTesseract is used for text extraction

For PDFs:

* PyMuPDF is used for digital PDF text extraction
* PDF2Image and PyTesseract are used for scanned PDF OCR

For videos:

* OpenCV is used to read video frames
* PyTesseract is used to extract text from selected frames
* Duplicate and noisy text is filtered to improve the output

---

### 5. AWS S3 Automation

The project also supports AWS S3-based automation.

The S3 workflow is:

```text
File uploaded to input/
        ↓
Scheduler detects the file
        ↓
Classifier identifies file type
        ↓
Correct OCR service is called
        ↓
Extracted text is saved as output
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

## How the FastAPI Flow Works

```text
User uploads a file through Swagger UI
        ↓
FastAPI route receives the uploaded file
        ↓
File is saved temporarily in temp/
        ↓
Related service function is called
        ↓
OCR processing is performed
        ↓
Extracted text is returned as JSON response
```

Example response:

```json
{
  "status": "success",
  "filename": "sample.pdf",
  "file_type": "pdf",
  "extracted_text": "Extracted text appears here"
}
```

---

## API Endpoints

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
4. Upload a file if required.
5. Click `Execute`.
6. Check the response body.

This allows image, PDF, and video APIs to be tested directly from the browser.

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

The project uses `.env` for configuration.

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

The classifier identifies the uploaded file type based on its extension and content.

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

## Current Status

Completed:

* Converted old OCR programs into a modular FastAPI package
* Added API routes for image, PDF, and video processing
* Added Swagger UI support
* Tested APIs successfully through Swagger UI
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

## Screenshots

### FastAPI Swagger UI

```text
screenshots/swagger_ui.png
```

### Image API Output

```text
screenshots/image_api_output.png
```

### PDF API Output

```text
screenshots/pdf_api_output.png
```

### Video API Output

```text
screenshots/video_api_output.png
```

### AWS S3 Input

```text
screenshots/s3_input.png
```

### AWS S3 Output

```text
screenshots/s3_output.png
```

### Scheduler Execution

```text
screenshots/scheduler.png
```

---

## Learning Outcome

Through this project, I learned how to build a backend OCR processing system using Python. I also understood how to organize code into a package structure, expose APIs using FastAPI, test APIs using Swagger UI, manage dependencies using a virtual environment, and connect the workflow with AWS S3 automation.

This project helped me understand how separate Python scripts can be converted into a more structured and maintainable backend application.

---

## Author

**Vedanti Hattarki**
