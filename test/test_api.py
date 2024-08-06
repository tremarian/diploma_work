import pytest
import allure
from pages.task_api import TaskApi
from pages import config


api = TaskApi(config.portal)


@allure.id("AGILE-API-1")
@allure.feature("Создание задачи")
@allure.severity("critical")
@allure.story("Создание задачи с валидными данными")
@allure.title("Заполнение обязательных полей")
@pytest.mark.api_test
@pytest.mark.parametrize('body_resuest, status_code', [
    ({
        'project_id': config.project_id,
        'workflow_stage_id': config.workflow_stage_id,
        'name': 'Заголовок задачи'
    }, 200)
    ])
def test_task_create_positive(body_resuest, status_code):
    with allure.step("Создать задачу"):
        task = api.task_create_json(body_resuest)
    with allure.step("Получить id созданной задачи из ответа запроса"):
        task_id = api.get_id(task)
    with allure.step("Получить созданную задачу по id"):
        status = api.get_task(task_id)
    with allure.step("Сравнить статус-код ответа на запрос с ожидаемым"):
        assert status == status_code


@allure.id("AGILE-API-2")
@allure.story("Создание задачи с невалидными данными")
@allure.severity("Major")
@allure.title("{title}")
@pytest.mark.api_test
@pytest.mark.xfail
@pytest.mark.parametrize('body_resuest, status_code, title', [
    ({}, 400, 'Без заполнения обязательных полей'),
    ({
        'project_id': config.project_id,
        'workflow_stage_id': config.workflow_stage_id,
        'priority': '60',
        'name': 'Задача с неверным id приоритета'
    }, 400, 'C неверным id приоритета'),
    ({
        'project_id': '999',
        'workflow_stage_id': config.workflow_stage_id,
        'name': 'Задача с неверным id проекта'
    }, 400, 'C неверным id проекта'),
    ({
        'project_id': config.project_id,
        'workflow_stage_id': '10',
        'name': 'Задача с неверным id этапа'
    }, 400, 'C неверным id этапа'),
    ({
        'project_id': config.project_id,
        'workflow_stage_id': config.workflow_stage_id,
        'epic_id': '99',
        'name': 'Задача с неверным id эпика'
    }, 400, 'C неверным id эпика')
    ])
def test_task_create_negative(body_resuest, status_code, title):
    with allure.step("Создать задачу"):
        task = api.task_create_status(body_resuest)
    with allure.step("Сравнить статус-код ответа на запрос с ожидаемым"):
        assert task == status_code
