import requests
from pages import config
import pytest
from pages.task_api import TaskApi
import json

url = TaskApi(config.portal)
@pytest.mark.api_test
def test_task_create_required():
    params = {
        'api_key': config.api_token
    }
    body = {
        'project_id': config.project_id,
        'workflow_stage_id': '1',
        'name': 'Заголовок задачи'
    }
    resp = requests.post(config.portal + 'api/v1/module/agile/issues/create', params=params, json=body)
    response1 = resp.json() # записывает ответ запроса и оформляет в словарь СРАЗУ
    response2 = response1['response'] 
    task_id = response2['id']

    resp2 = requests.get(f'{config.portal}api/v1/module/agile/issues/get/{task_id}')
    assert resp2.status_code == 200

    
    # получить задачу https://{company}.aspro.cloud/api/v1/module/agile/issues/get/{id}

@pytest.mark.api_test
def test_task_create_not_required():
    params = {
        'api_key': config.api_token
    }
    body = {}
    resp = requests.post(config.portal + 'api/v1/module/agile/issues/create', params=params, json=body)
    assert resp.status_code == 400