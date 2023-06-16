import time
import testit


@testit.step('Generate full logs')
def generate_logs() -> str:
    time.sleep(1)
    return "some strings"


@testit.step('Generate empty logs')
def generate_empty_logs() -> str:
    time.sleep(1)
    return ""


@testit.externalId("test_log_success")
@testit.displayName("Log success")
@testit.description("Check correct logs")
@testit.labels("success", "logs")
@testit.workItemIds("1523")
def test_log_success():
    logs = generate_logs()
    assert len(logs) > 0


@testit.externalId("test_log_failed")
@testit.displayName("Log failed")
@testit.description("Check incorrect logs")
@testit.labels("failed", "logs")
@testit.link(url='https://google.com', title='Bug-321', description='Logs bug', type='Issue')
def test_log_failed():
    logs = generate_empty_logs()
    assert len(logs) > 0
