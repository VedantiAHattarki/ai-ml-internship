function OCRResult({

  responseData,
  text

}) {

  const wordCount = text
    ? text.trim().split(/\s+/).length
    : 0;

  const characterCount = text.length;

  return (

    <>

      {responseData && (

        <div className="details">

          <h3>OCR Details</h3>

          <p>

            <strong>Status :</strong> {responseData.status}

          </p>

          <p>

            <strong>Filename :</strong> {responseData.filename}

          </p>

          <p>

            <strong>File Type :</strong> {responseData.file_type}

          </p>

          <p>

            <strong>Characters :</strong> {characterCount}

          </p>

          <p>

            <strong>Words :</strong> {wordCount}

          </p>

        </div>

      )}

      <h3>Extracted Text</h3>

      <textarea

        rows="18"

        value={text}

        readOnly

        placeholder="OCR output will appear here..."

      />

    </>

  );

}

export default OCRResult;