from flask import Blueprint, request, jsonify
from app.utils.file_utils import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf

pdf_bp = Blueprint("pdf", __name__)


@pdf_bp.route("/process-pdf", methods=["POST"])
def process_pdf():
    file_path, error = save_uploaded_file(request)

    if error:
        return jsonify({"error": error}), 400

    text = extract_text_from_pdf(file_path)

    return jsonify({"text": text})