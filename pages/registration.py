from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        alert = self._driver.find_element(By.CSS_SELECTOR, '.alert')
        return alert.text()
    # def click_seven(self):
    #     self._driver.find_element(
    #             By.CSS_SELECTOR, '.keys span:nth-child(1)'
    #         ).click()

    # def click_plus(self):
    #     self._driver.find_element(
    #         By.CSS_SELECTOR, '.keys span:nth-child(4)'
    #     ).click()

    # def click_eight(self):
    #     self._driver.find_element(
    #         By.CSS_SELECTOR, '.keys span:nth-child(2)'
    #     ).click()

    # def click_equal(self):
    #     self._driver.find_element(
    #         By.CSS_SELECTOR, '.keys span:nth-child(15)'
    #     ).click()

    # def text_result(self, time):
    #     time = int(time)
    #     WebDriverWait(self._driver, time+3).until(
    #         EC.text_to_be_present_in_element(
    #             (By.CSS_SELECTOR, "div.screen"), "15"
    #             )
    #         )
    #     text = self._driver.find_element(By.CSS_SELECTOR, '.screen').text
    #     return text
