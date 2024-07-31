from selenium.webdriver.common.by import By


class Auth:
    """
        Класс для работы со страницей авторизации и выбора портала.
    """
    # кука s1
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://my.asproagile.ru/"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self):
        """
            Метод для авторизации.
            Ищет поля логина и пароля, вводит в них заданные значений
            и выполняет авторизацию.
        """
        email_input = self._driver.find_element(By.NAME, 'email')
        email_input.send_keys('tremariansch@gmail.com')

        password_input = self._driver.find_element(By.NAME, 'password')
        password_input.send_keys('G51piAvu')

        submit = self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()

    def choose_portal(self):
        """
            Метод выбирает портал для авторизации.
        """
        portal = self._driver.find_element(
            By.CSS_SELECTOR, '.select-product__tabs a:nth-child(2)'
            )
        portal.click()
        url = self._driver.current_url
        return url

    def qick_auth(self):
        """
            Метод для быстрой авторизации
        """


    def get_auth_cookie (self, cookie):
        """
            Попытка получить куки
        """
        token = self._driver.get_cookie(cookie)
        return token
    
    def delete_cookie(self):
        self._driver.delete_all_cookies()

    def add_cookie (self, cookie):
        self._driver.add_cookie(cookie)
        self._driver.refresh()

