from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Task:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://diploma.asproagile.ru/_module/agile/view/backlog/1"
            )
        self._driver.implicitly_wait(4)


    def click_create_button(self):
        create_issue = self._driver.find_element(By.CSS_SELECTOR, '[data-create-issue=""]')
        create_issue.click()


    def fill_title(self, name):
        input = self._driver.find_element(By.CSS_SELECTOR, '.agile-issue-form [name="name"]')
        input.click()
        input.send_keys(name)


    def click_submit(self):
        button = self._driver.find_element(By.CSS_SELECTOR, '.btn-success')
        button.click()


    def click_toast(self):
        toast = self._driver.find_element(By.CSS_SELECTOR, '.toast-success')
        toast.click()


    def get_task_title(self):
        self._driver.implicitly_wait(4)
        name = self._driver.find_element(By.CSS_SELECTOR, '.sidepanel .page-bar__title-inner .component-editable__content-inner')
        text = name.get_attribute("title")
        # sleep(10)
        return text
        