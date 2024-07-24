from selenium import webdriver
from pages.registration import Registration


def test_registration_without_filling_email():
    browser = webdriver.Chrome()
    registration = Registration(browser)
    registration.set_login('')
    registration.set_password('123456')
    registration.click_submit()

    assert registration.alert_text == 'Email обязателен для заполнения'
