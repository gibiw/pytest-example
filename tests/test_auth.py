import time


def set_login(login: str):
    time.sleep(1)
    pass


def set_password(password: str):
    time.sleep(1)
    assert password == "Qwerty123"


def click_login_button():
    time.sleep(1)
    pass


def test_success_auth():
    set_login("user01")
    set_password("Qwerty123")
    click_login_button()
    pass


def test_failed_auth():
    set_login("user01")
    set_password("Qwerty321")
    click_login_button()
    pass
