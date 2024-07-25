from selenium.webdriver.common.by import By


class Auth:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://my.asproagile.ru/"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self):
        email_input = self._driver.find_element(By.NAME, 'email')
        email_input.send_keys('tremariansch@gmail.com')

        password_input = self._driver.find_element(By.NAME, 'password')
        password_input.send_keys('G51piAvu')

        submit = self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()

    def choose_portal(self):
        portal = self._driver.find_element(
            By.CSS_SELECTOR, '.select-product__tabs a:nth-child(2)'
            )
        portal.click()
        url = self._driver.current_url
        return url

    def qick_auth(self):
        email_input = self._driver.find_element(By.NAME, 'email')
        email_input.send_keys('tremariansch@gmail.com')

        password_input = self._driver.find_element(By.NAME, 'password')
        password_input.send_keys('G51piAvu')

        submit = self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()

        portal = self._driver.find_element(
            By.CSS_SELECTOR, '.select-product__tabs a:nth-child(2)'
            )
        portal.click()
