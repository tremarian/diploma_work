import allure
from selenium.webdriver.common.by import By
from pages import config


class Auth:
    """
        Класс для работы со страницей и токеном авторизации в ui-тестах.
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            config.portal
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("ui. Авторизация через пользовательский интерфейс")
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

    @allure.step("ui. Получение текущего url страницы и возврат значения")
    def get_current_url(self) -> str:
        """
            Метод получает текущий url страницы
            и возвращает полученное значение.
        """
        url = self._driver.current_url
        return url

    @allure.step("ui. Получение значения указанной куки и возврат значения")
    def get_auth_cookie(self, cookie: dict) -> dict:
        """
            Метод получает значение указанной куки,
            сохраняет его в переменную и возвращает.
        """
        token = self._driver.get_cookie(cookie)
        return token

    @allure.step("ui. Удаление всех куки")
    def delete_cookie(self):
        """
            Метод удаляет все куки.
        """
        self._driver.delete_all_cookies()

    @allure.step("ui. Добавление указанной куки и обновление страницы")
    def add_cookie(self, cookie: dict):
        """
            Метод добавляет указанную куки и обновляет страницу.
        """
        self._driver.add_cookie(cookie)
        self._driver.refresh()
