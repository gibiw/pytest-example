import time


def generate_logs() -> str:
    time.sleep(1)
    return "some strings"


def generate_empty_logs() -> str:
    time.sleep(1)
    return ""


def test_log_success():
    logs = generate_logs()
    assert len(logs) > 0


def test_log_failed():
    logs = generate_empty_logs()
    assert len(logs) > 0

