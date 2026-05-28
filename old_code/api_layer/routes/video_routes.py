from flask import Blueprint, request, jsonify
from app.utils.file_utils import save_uploaded_file
from app.services.video_service import extract_text_from_video

video_bp = Blueprint("video", __name__)


@video_bp.route("/process-video", methods=["POST"])
def process_video():
    file_path, error = save_uploaded_file(request)

    if error:
        return jsonify({"error": error}), 400

    text = extract_text_from_video(file_path)

    return jsonify({"text": text})