from src.processor import process_batch

def test_process_batch():
    result = process_batch([10, 20, 30])

    assert result["count"] == 3
    assert result["average"] == 20
