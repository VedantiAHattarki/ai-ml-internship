import {
  FaImage,
  FaFilePdf,
  FaVideo
} from "react-icons/fa";

function FileUpload({

  ocrType,
  setOcrType,
  setFile,
  clearAll

}) {

  return (

    <>

      <h3>Select OCR Type</h3>

      <div className="ocr-options">

        <label className={ocrType === "image" ? "active-card" : ""}>

          <input
            type="radio"
            value="image"
            checked={ocrType === "image"}
            onChange={(e) => {

              setOcrType(e.target.value);
              clearAll();

            }}
          />

          <FaImage size={35} />

          <p>Image OCR</p>

        </label>

        <label className={ocrType === "pdf" ? "active-card" : ""}>

          <input
            type="radio"
            value="pdf"
            checked={ocrType === "pdf"}
            onChange={(e) => {

              setOcrType(e.target.value);
              clearAll();

            }}
          />

          <FaFilePdf size={35} />

          <p>PDF OCR</p>

        </label>

        <label className={ocrType === "video" ? "active-card" : ""}>

          <input
            type="radio"
            value="video"
            checked={ocrType === "video"}
            onChange={(e) => {

              setOcrType(e.target.value);
              clearAll();

            }}
          />

          <FaVideo size={35} />

          <p>Video OCR</p>

        </label>

      </div>

      <div className="drop-area">

        <h3>Upload File</h3>

        <p>Select the file to extract text.</p>

        <input

          id="fileInput"

          type="file"

          accept={{
            image: "image/*",
            pdf: ".pdf",
            video: "video/*"
          }[ocrType]}

          onChange={(e) => {

            if (e.target.files.length > 0) {

              setFile(e.target.files[0]);

            }

          }}

        />

      </div>

    </>

  );

}

export default FileUpload;