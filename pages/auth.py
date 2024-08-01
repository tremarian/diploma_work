from selenium.webdriver.common.by import By
from pages import config


class Auth:
    """
        Класс для работы со страницей авторизации и выбора портала.
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            config.portal
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
        email_input.send_keys(config.user_login)

        password_input = self._driver.find_element(By.NAME, 'password')
        password_input.send_keys(config.user_password)

        submit = self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()

    def get_current_url(self):
        """
            Метод получает текущий url страницы
            и возвращает полученное значение.
        """
        url = self._driver.current_url
        return url

    def get_auth_cookie(self, cookie):
        """
            Метод получает значение указанной куки,
            сохраняет его в переменную и возвращает.
        """
        token = self._driver.get_cookie(cookie)
        return token

    def delete_cookie(self):
        self._driver.delete_all_cookies()

    def add_cookie(self, cookie):
        self._driver.add_cookie(cookie)
        self._driver.refresh()
