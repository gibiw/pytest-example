import time

import testit


@testit.step('Enter login', 'Enter login to textbox')
def set_login(login: str):
    testit.addAttachments(data=login, is_text=True, name='login.txt')
    time.sleep(1)
    pass


@testit.step('Enter password')
def set_password(password: str):
    time.sleep(1)
    assert password == "Qwerty123"


@testit.step
def click_login_button():
    time.sleep(1)
    pass


@testit.externalId("test_success_auth")
@testit.displayName("Auth success")
@testit.description("Check auth with valid creds")
@testit.labels("success", "auth")
def test_success_auth():
    set_login("user01")
    set_password("Qwerty123")
    click_login_button()
    pass


@testit.externalId("test_failed_auth")
@testit.displayName("Auth failed")
@testit.description("Check auth with invalid creds")
@testit.labels("failed", "auth")
@testit.link(url='https://ya.ru', title='Bug-123', description='Auth bug', type='Issue')
def test_failed_auth():
    set_login("user01")
    set_password("Qwerty321")
    click_login_button()
    pass
