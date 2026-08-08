import FileUpload from "./FileUpload";
import Buttons from "./Buttons";

function UploadForm({

  ocrType,
  setOcrType,
  setFile,
  clearAll,

  uploadFile,
  downloadJSON,
  copyText,

  loading

}) {

  return (

    <>

      <FileUpload

        ocrType={ocrType}
        setOcrType={setOcrType}
        setFile={setFile}
        clearAll={clearAll}

      />

      <Buttons

        uploadFile={uploadFile}
        downloadJSON={downloadJSON}
        copyText={copyText}
        clearAll={clearAll}
        loading={loading}

      />

    </>

  );

}

export default UploadForm;