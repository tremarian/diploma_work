from selenium import webdriver
from pages.registration import Registration
from pages.auth import Auth

# def test_registration_without_filling_email():
#     browser = webdriver.Chrome()
#     registration = Registration(browser)
#     registration.set_login('')
#     registration.set_password('123456')
#     registration.click_submit()

#     assert registration.alert_text == 'Email обязателен для заполнения'

def test_positive_auth():
    browser = webdriver.Chrome()
    auth = Auth(browser)
    auth.authorization()
    assert auth.choose_portal() == 'https://diploma.asproagile.ru/'

