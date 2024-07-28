from selenium import webdriver
from pages.auth import Auth
from pages.task import Task
import pytest


# @pytest.mark.ui_test
# def test_positive_auth():
#     """
#         Функция для проверки авторизации на протале с валидными данными.
#     """
#     browser = webdriver.Chrome()
#     auth = Auth(browser)
#     auth.authorization()
#     assert auth.choose_portal() == 'https://diploma.asproagile.ru/'


@pytest.mark.ui_test
@pytest.mark.parametrize('title', [
    ('Название на кириллице'),
    ('Latin name')
    ])
def test_task_create(title):
    """
        Функция для проверки создания задачи с валидными заголовком.
    """
    browser = webdriver.Chrome()
    auth = Auth(browser)
    auth.qick_auth()

    task = Task(browser)
    task.click_create_button()

    task.fill_title(title)
    task.click_submit()
    task.click_toast()

    assert task.get_task_title() == title


# @pytest.mark.ui_test
# @pytest.mark.parametrize('estimate, result', [
#     ('1.5', '1.5'),
#     ('1,5', '1'),
#     ('1.3', '1.5')
#     ])
# def test_fill_estimate(estimate, result):
#     """
#         Функция для проверки заполнения трудозатрат при создании задачи.
#     """
#     browser = webdriver.Chrome()
#     auth = Auth(browser)
#     auth.qick_auth()

#     task = Task(browser)
#     task.click_create_button()
#     title = 'Заголовок задачи'
#     task.fill_title(title)
#     task.fill_estimate(estimate)
#     task.click_submit()
#     task.click_toast()

#     assert task.get_task_estimate() == result
