import {
  FaPlay,
  FaDownload,
  FaCopy,
  FaTrash
} from "react-icons/fa";

function Buttons({

  uploadFile,
  downloadJSON,
  copyText,
  clearAll,
  loading

}) {

  return (

    <div className="button-group">

      <button onClick={uploadFile}>

        <FaPlay />

        {loading ? " Processing..." : " Process OCR"}

      </button>

      <button onClick={downloadJSON}>

        <FaDownload />

        {" "}Download JSON

      </button>

      <button onClick={copyText}>

        <FaCopy />

        {" "}Copy Text

      </button>

      <button onClick={clearAll}>

        <FaTrash />

        {" "}Clear

      </button>

    </div>

  );

}

export default Buttons;