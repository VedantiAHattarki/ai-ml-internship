from flask import Blueprint, request, jsonify
from api_layer.utils.request_handler import save_uploaded_file
from digitalpdf_to_text.pdf_to_text import extract_text_from_pdf

pdf_bp = Blueprint("pdf", __name__)


@pdf_bp.route("/process-pdf", methods=["POST"])
def process_pdf():
    file_path, error = save_uploaded_file(request)

    if error:
        return jsonify({"error": error}), 400

    text = extract_text_from_pdf(file_path)

    return jsonify({"text": text})