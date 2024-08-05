import requests
from pages import config
import pytest
from pages.task_api import TaskApi

url = TaskApi(config.portal)

@pytest.mark.api_test
def test_task_create():
    params = {
        'api_key': config.api_token
    }
    body = {
        'project_id': config.project_id,
        'workflow_stage_id': '1',
        'name': 'Заголовок задачи'
    }
    resp = requests.post(config.portal + 'api/v1/module/agile/issues/create', params=params, json=body)
    response = resp.json()
    task_id = response.get('id')

    resp2 = requests.get(f'{config.portal}api/v1/module/agile/issues/get/{task_id}')
    assert resp2.status_code == 200

    
    # получить задачу https://{company}.aspro.cloud/api/v1/module/agile/issues/get/{id}