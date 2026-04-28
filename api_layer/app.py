from flask import Flask
from api_layer.routes.pdf_routes import pdf_bp
from api_layer.routes.image_routes import image_bp
from api_layer.routes.video_routes import video_bp

app = Flask(__name__)

app.register_blueprint(pdf_bp)
app.register_blueprint(image_bp)
app.register_blueprint(video_bp)


@app.route("/", methods=["GET"])
def home():
    return {
        "message": "AI/ML OCR Flask API is running",
        "endpoints": [
            "/process-pdf",
            "/process-image",
            "/process-video"
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)