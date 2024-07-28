from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Task:
    """
        Класс для работы со страницей бэклога
        в Agile-проектах.
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://diploma.asproagile.ru/_module/agile/view/backlog/1"
            )
        self._driver.implicitly_wait(4)

    def click_create_button(self):
        """
            Метод ищет кнопку создания задачи на странице Agile-проекта.
            После нахождения кнопки по ней выполняется клик.
        """
        create_issue = self._driver.find_element(
            By.CSS_SELECTOR, '[data-create-issue=""]'
            )
        create_issue.click()

    def fill_title(self, name: str):
        """
            Метод в качестве параметра принимает название для задачи.
            Ожидает появления поля для ввода в течении 5 секунд.
            Выполняет клик по найденному полю
            и вводит в поле переданный параметр названия.
        """
        WebDriverWait(self._driver, "5").until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.agile-issue-form [name="name"]')
                )
            )
        input = self._driver.find_element(
            By.CSS_SELECTOR, '.agile-issue-form [name="name"]'
            )
        input.click()
        input.send_keys(name)

    def click_submit(self):
        """
            Метод ищет кнопку сохранения формы создания задачи
            и кликает на нее.
        """
        button = self._driver.find_element(By.CSS_SELECTOR, '.btn-success')
        button.click()

    def click_toast(self):
        """
            Метод ищет уведомление об успешном создании задачи
            и кликает на него.
        """
        toast = self._driver.find_element(By.CSS_SELECTOR, '.toast-success')
        toast.click()

    def get_task_title(self) -> str:
        """
            Метод получает название задачи, открытой в слайдпанели.
            Возвращает название в виде строки.
        """
        self._driver.implicitly_wait(4)
        name = self._driver.find_element(
            By.CSS_SELECTOR,
            '.sidepanel .page-bar__title-inner .component-editable__content-inner'
            # '.sidepanel .page-title span'
            )
        text = name.get_attribute("title")
        return text

    def fill_estimate(self, estimate: str):
        """
            Метод для заполнения поля «Трудозатрат» в форме создания задачи.
            В качестве параметра принимает трудозатраты.
            Ищет поле трудозатрат, кликает на него.
            Заполяет поле значением из параметра.
        """
        input = self._driver.find_element(
            By.CSS_SELECTOR, '.agile-issue-form [name="estimate"]'
            )
        input.click()
        input.clear()
        input.send_keys(estimate)

    def get_task_estimate(self) -> str:
        """
            Метод получает трудозатраты задачи, открытой в слайдпанели.
            Возвращает трудозатраты в виде строки.
        """
        self._driver.implicitly_wait(4)
        name = self._driver.find_element(
            By.CSS_SELECTOR, '[data-estimate] span'
            )
        text = name.get_attribute("title")
        return text
