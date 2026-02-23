from app import generate_log

def test_generate_log():
    result = generate_log()
    assert result == "Application started successfully"