import requests
from pages import config


class TaskApi:
    def __init__(self, url):
        self.url = url

    def task_create(self, project_id, workflow_stage_id, name):
        params = {
            'api_key': config.api_token
        }
        body = {
            'project_id': project_id,
            'workflow_stage_id': workflow_stage_id,
            'name': name
        }
        resp = requests.post(self.url + 'api/v1/module/agile/issues/create', params=params, json=body)
        return resp.json()
    # получить задачу https://{company}.aspro.cloud/api/v1/module/agile/issues/get/{id}