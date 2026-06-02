def sample_text_processing():
    text = "Artificial Intelligence and OCR based text extraction system"
    return text.lower().split()


def test_sample_text_processing_benchmark(benchmark):
    result = benchmark(sample_text_processing)

    assert result == [
        "artificial",
        "intelligence",
        "and",
        "ocr",
        "based",
        "text",
        "extraction",
        "system"
    ]