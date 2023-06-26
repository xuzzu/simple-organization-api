import time
from locust import HttpUser, task, between

"""
Стресс-тест для API должностей и дерева организации. Класс Testing наследуется от Locust, 
который отправляет запросы на эти эндпоинты и измеряет время ответа. Для каждого эндпоинта определены две задачи: 
получение и создание объектов. 
Результаты теста записываются в файл results.txt.
"""

class Testing(HttpUser):
    wait_time = between(1, 2)
    host = 'http://localhost:8000'

    # Стресс-тест должностей
    @task
    def get_positions(self):
        start_time = time.time()
        response = self.client.get('/api/position/')
        response_time = time.time() - start_time
        self.log_response_time('get_positions', response_time)
        if response.status_code != 200:
            print(f'Error: {response.status_code}')

    @task
    def create_position(self):
        payload = {
            'pos_name': 'Analyst',
            'salary': 50000,
        }
        start_time = time.time()
        response = self.client.post('/api/position/', json=payload)
        response_time = time.time() - start_time
        self.log_response_time('create_position', response_time)
        if response.status_code != 201:
            print(f'Error: {response.status_code}')

    # Стресс-тест дерева организации
    @task
    def get_structure(self):
        start_time = time.time()
        response = self.client.get('/api/organization-structure/')
        response_time = time.time() - start_time
        self.log_response_time('get_positions', response_time)
        if response.status_code != 200:
            print(f'Error: {response.status_code}')

    def log_response_time(self, endpoint, response_time):
        with open('load_test_results.txt', 'a+') as f:
            f.write(f'{endpoint}: {response_time}\n')