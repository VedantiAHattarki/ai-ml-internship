import timeit


def test_timeit_text_processing():
    execution_time = timeit.timeit(
        stmt="'Artificial Intelligence OCR Project'.lower().split()",
        number=1000
    )

    assert execution_time >= 0
    print(f"Execution time for 1000 runs: {execution_time}")