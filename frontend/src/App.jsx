import { useState } from "react";

import api from "./api";
import "./App.css";

import Navbar from "./components/Navbar";
import UploadForm from "./components/UploadForm";
import OCRResult from "./components/OCRResult";
import LoadingSpinner from "./components/LoadingSpinner";
import Footer from "./components/Footer";

function App() {

  const [ocrType, setOcrType] = useState("image");
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const endpoint = {
      image: "/api/image/process",
      pdf: "/api/pdf/process",
      video: "/api/video/process",
    }[ocrType];

    try {

      setLoading(true);

      const response = await api.post(endpoint, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setResponseData(response.data);

      setText(response.data.extracted_text || "");

    } catch (error) {

      console.error(error);

      alert(
        error.response?.data?.detail ||
          "Unable to process the selected file."
      );

    } finally {

      setLoading(false);

    }

  };

  const downloadJSON = () => {

    if (!responseData) {
      alert("No OCR result available.");
      return;
    }

    const blob = new Blob(
      [JSON.stringify(responseData, null, 4)],
      {
        type: "application/json",
      }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "ocr_result.json";

    a.click();

    URL.revokeObjectURL(url);

  };

  const copyText = () => {

    if (!text) {
      alert("Nothing to copy.");
      return;
    }

    navigator.clipboard.writeText(text);

    alert("Text copied successfully.");

  };

  const clearAll = () => {

    setFile(null);
    setText("");
    setResponseData(null);

    const input = document.getElementById("fileInput");

    if (input) {
      input.value = "";
    }

  };

  return (

    <>

      <Navbar />

      <div className="container">

        <UploadForm

          ocrType={ocrType}
          setOcrType={setOcrType}
          setFile={setFile}
          clearAll={clearAll}

          uploadFile={uploadFile}
          downloadJSON={downloadJSON}
          copyText={copyText}
          loading={loading}

        />

        {loading && <LoadingSpinner />}

        <OCRResult

          responseData={responseData}
          text={text}

        />

      </div>

      <Footer />

    </>

  );

}

export default App;