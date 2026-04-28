import mimetypes

def classify_file(file_path):
    file_type, _ = mimetypes.guess_type(file_path)

    if file_type:
        if "pdf" in file_type:
            return "pdf"
        elif "image" in file_type:
            return "image"
        elif "video" in file_type:
            return "video"

    return "unknown"