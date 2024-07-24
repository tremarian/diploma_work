from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Registration:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://my.asproagile.ru/register/agile"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_login(self, login):
        login_input = self._driver.find_element(By.NAME, 'email')
        login_input.send_keys(login)


    def set_password(self, password):
        password_input = self._driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)

    def click_submit(self):
        submit_button = self._driver.find_element(By.ID, 'form-submit')
        submit_button.click()
    

    def alert_text(self):
        text = self._driver.find_element(By.CSS_SELECTOR, '.alert').text
        return text
    
