from flask import Blueprint, request, jsonify
from app.utils.file_utils import save_uploaded_file
from app.services.image_service import extract_text_from_image

image_bp = Blueprint("image", __name__)


@image_bp.route("/process-image", methods=["POST"])
def process_image():
    file_path, error = save_uploaded_file(request)

    if error:
        return jsonify({"error": error}), 400

    text = extract_text_from_image(file_path)

    return jsonify({"text": text})