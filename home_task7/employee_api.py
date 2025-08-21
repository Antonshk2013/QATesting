import requests

class EmployeeApi:
    """Класс для работы с API сотрудников"""

    def __init__(self, url):
        """Инициализация с базовым URL"""
        self.url = url
    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active=True):
        """Создание нового сотрудника"""
        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        resp = requests.post(f"{self.url}/employee/create", json=employee_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    def get_employee(self, employee_id):
        """Получение информации о сотруднике по ID"""
        resp = requests.get(f"{self.url}/employee/info?id={employee_id}")
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    def update_employee(self, employee_id, **kwargs):
        """Изменение данных сотрудника (передаются только изменяемые параметры)"""
        update_data = {key: value for key, value in kwargs.items() if value is not None}

        resp = requests.patch(f"{self.url}/employee/change?id={employee_id}", json=update_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()