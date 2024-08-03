from selenium import webdriver
from pages.auth import Auth
from pages.task import Task
import pytest
from pages import config
import allure


@allure.id("AGILE-1")
@allure.feature("Авторизация")
@allure.severity("blocker")
@allure.title("Авторизация с валидными данными")
@pytest.mark.ui_test
def test_positive_auth():
    """
        Функция для проверки авторизации на протале с валидными данными.
    """
    with allure.step("Открыть портал"):
        browser = webdriver.Chrome()
        auth = Auth(browser)
    with allure.step("Ввести авторизационные данные, нажать кнопку «Войти»"):
        auth.authorization()
    with allure.step("Получить токен авторизации"):
        config.auth_token = auth.get_auth_cookie('s1')
    with allure.step("Сравнить текущий url с заданным порталом"):
        assert auth.get_current_url() == config.portal

@allure.id("AGILE-2")
@allure.feature("Создание задачи")
@allure.story("С указанием валидного названия")
@allure.severity("critical")
@allure.title("С указанием названия «{title}»")
@pytest.mark.ui_test
@pytest.mark.parametrize('title', [
    ('Название на кириллице'),
    ('Latin name')
    ])
def test_task_create(title):
    """
        Функция для проверки создания задачи с валидными заголовком.
    """
    with allure.step("Открыть портал"):
        browser = webdriver.Chrome()
        auth = Auth(browser)
    with allure.step("Авторизоваться"):
        with allure.step("Очистить куки"):
            auth.delete_cookie()
        with allure.step("Добавить токен авторизации в куки"):
            auth.add_cookie(config.auth_token)
    with allure.step("Создать задачу"):
        with allure.step("Открыть бэклог"):
            task = Task(browser)
        with allure.step("Нажать кнопку создания задачи"):
            task.click_create_button()
        with allure.step("Заполнить заголовок задачи"):
            task.fill_title(title)
        with allure.step("Нажать кнопку сохранения"):
            task.click_submit()
    with allure.step("Открыть созданную задачу по клику на увекдомление"):
        task.click_toast()
    with allure.step("Сравнить заголовок задачи с заданным"):
        assert task.get_task_title() == title

@allure.id("AGILE-2")
@allure.feature("Создание задачи")
@allure.story("С указанием трудозатрат")
@allure.severity("critical")
@allure.title("С указанием трудозатрат «{estimate}»")
@pytest.mark.ui_test
@pytest.mark.parametrize('estimate, result', [
    ('1.5', '1.5'),
    ('1,5', '1'),
    ('1.3', '1.5')
    ])
def test_fill_estimate(estimate, result):
    """
        Функция для проверки заполнения трудозатрат при создании задачи.
    """
    with allure.step("Открыть портал"):
        browser = webdriver.Chrome()
        auth = Auth(browser)
    with allure.step("Авторизоваться"):
        with allure.step("Очистить куки"):
            auth.delete_cookie()
        with allure.step("Добавить токен авторизации в куки"):
            auth.add_cookie(config.auth_token)
    with allure.step("Создать задачу"):
        with allure.step("Открыть бэклог"):
            task = Task(browser)
        with allure.step("Нажать кнопку создания задачи"):
            task.click_create_button()
        with allure.step("Заполнить заголовок задачи"):
            title = 'Заголовок задачи'
            task.fill_title(title)
        with allure.step("Заполнить трудозатраты задачи"):
            task.fill_estimate(estimate)
        with allure.step("Нажать кнопку сохранения"):
            task.click_submit()
    with allure.step("Открыть созданную задачу по клику на увекдомление"):
        task.click_toast()
    with allure.step("Сравнить трудозатраты задачи с заданными"):
        assert task.get_task_estimate() == result
