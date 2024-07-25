from selenium import webdriver
from pages.auth import Auth
from pages.task import Task
import pytest

# Авторизация с валидными данными
# def test_positive_auth():
#     browser = webdriver.Chrome()
#     auth = Auth(browser)
#     auth.authorization()
#     assert auth.choose_portal() == 'https://diploma.asproagile.ru/'


# Создание задачи с заголовком на кириллице
# Проработать 2 запуск
# @pytest.mark.parametrize('title', [
#     ('Название на кириллице'),
#     ('Latin name')
#     ])
def test_task_create():
    browser = webdriver.Chrome()
    auth = Auth(browser)
    auth.qick_auth()

    task = Task(browser)
    task.click_create_button()

    title = 'Название на кириллице'
    task.fill_title(title)
    task.click_submit()
    task.click_toast()

    assert task.get_task_title() == title



# Создание задачи с дробными трудозатратами
# с использованием точки в качестве разделителя

# Создание задачи с дробными трудозатратами
# с использованием запятой в качестве разделителя

# Создание задачи с дробными трудозатрами не кратным 0.5
