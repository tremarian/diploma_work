import requests
import allure
from pages import config


class TaskApi:
    """
        Класс для работы с задачами с помощью api.
    """
    def __init__(self, url):
        self.url = url

    @allure.step("api. Создание задачи и возвращение тела ответа")
    def task_create_json(self, body: dict) -> dict:
        """
            Метод создает задачу с переданными параметрами
            и возвращает тело ответа справочником.
        """
        params = {
            'api_key': config.api_token
        }

        resp = requests.post(
            self.url + 'api/v1/module/agile/issues/create',
            params=params, json=body
            )
        return resp.json()

    @allure.step(
            "api. Получение задачи по переданному idи возвращение статус кода"
            )
    def get_task(self, id: int) -> int:
        """
            Метод принимает id задачи,
            получает задачу по указанному id
            и возвращает статус-код ответа.
        """
        params = {
            'api_key': config.api_token
        }
        resp = requests.get(
            f'{self.url}api/v1/module/agile/issues/get/{id}', params=params
            )
        return resp.status_code

    @allure.step("api. Получение значения id из тела ответа")
    def get_id(self, body: dict) -> int:
        """
            Метод принимаем справочник,
            извлекает и возвращает id.
        """
        first_item = body['response']
        task_id = first_item['id']
        return task_id

    @allure.step("api. Создание задачи и возвращение статус-кода ответа")
    def task_create_status(self, body: dict) -> int:
        """
            Метод создает задачу с переданными параметрами
            и возвращает статус-код ответа.
        """
        params = {
            'api_key': config.api_token
        }

        resp = requests.post(
            self.url + 'api/v1/module/agile/issues/create',
            params=params, json=body
            )
        return resp.status_code
