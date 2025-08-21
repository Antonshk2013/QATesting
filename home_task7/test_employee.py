from employee_api import EmployeeApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_create_employee():
    """Тест: создание нового сотрудника"""

    # 1. Создаём сотрудника
    employee = api.create_employee(
        first_name="John",
        last_name="Doe",
        middle_name="Edward",
        company_id=1,
        email="johndoe@example.com",
        phone="+1234567890",
        birthdate="1990-01-15",
        is_active=True
    )
    # 2. Проверяем, что ID созданного сотрудника есть в ответе
    # assert "id" in employee, "Ожидалось наличие ключа 'id' в ответе"
    # 3. Проверяем, что данные сотрудника соответствуют отправленным
    assert employee["first_name"] == "John", f"Ожидалось 'John', получено '{employee['first_name']}'"
    assert employee["last_name"] == "Doe", f"Ожидалось 'Doe', получено '{employee['last_name']}'"
    assert employee["middle_name"] == "Edward", f"Ожидалось 'Edward', получено '{employee['middle_name']}'"
    assert employee["company_id"] == 1, f"Ожидалось 1, получено '{employee['company_id']}'"
    assert employee["email"] == "johndoe@example.com", f"Ожидалось 'johndoe@example.com', получено '{employee['email']}'"
    assert employee["phone"] == "+1234567890", f"Ожидалось '+1234567890', получено '{employee['phone']}'"
    assert employee["birthdate"] == "1990-01-15", f"Ожидалось '1990-01-15', получено '{employee['birthdate']}'"
    assert employee["is_active"] is True, "Ожидалось, что сотрудник активен"
    # print(f"Тест пройден: сотрудник {employee['id']} успешно создан.")

def test_get_employee_info():
    """Тест: получение информации о сотруднике"""

    # 1. Создаём нового сотрудника
    employee = api.create_employee(
        first_name="Alice",
        last_name="Brown",
        middle_name="Marie",
        company_id=2,
        email="alicebrown@example.com",
        phone="+9876543210",
        birthdate="1988-05-22",
        is_active=True
    )
    employee_id = employee["id"]
    # 2. Запрашиваем информацию о сотруднике
    retrieved_employee = api.get_employee(employee_id)
    # 3. Проверяем, что данные совпадают
    assert retrieved_employee["id"] == employee_id, f"Ожидался ID {employee_id}, получено {retrieved_employee['id']}"
    assert retrieved_employee["first_name"] == "Alice", f"Ожидалось 'Alice', получено '{retrieved_employee['first_name']}'"
    assert retrieved_employee["last_name"] == "Brown", f"Ожидалось 'Brown', получено '{retrieved_employee['last_name']}'"
    assert retrieved_employee["email"] == "alicebrown@example.com", f"Ожидалось 'alicebrown@example.com', получено '{retrieved_employee['email']}'"

    print(f"Тест пройден: информация о сотруднике {employee_id} получена корректно.")
def test_update_employee():
    """Тест: изменение данных о сотруднике"""

    # 1. Создаём сотрудника
    employee = api.create_employee(
        first_name="Bob",
        last_name="Smith",
        middle_name="James",
        company_id=3,
        email="bobsmith@example.com",
        phone="+1357924680",
        birthdate="1985-07-30",
        is_active=True
    )
    employee_id = employee["id"]
    # 2. Обновляем данные
    updated_employee = api.update_employee(
        employee_id,
        first_name="Robert",
        email="robertsmith@example.com",
        is_active=False
    )
    # 3. Проверяем, что данные изменились
    assert updated_employee["first_name"] == "Robert", f"Ожидалось 'Robert', получено '{updated_employee['first_name']}'"
    assert updated_employee["email"] == "robertsmith@example.com", f"Ожидалось 'robertsmith@example.com', получено '{updated_employee['email']}'"
    assert updated_employee["is_active"] is False, "Ожидалось, что сотрудник будет неактивным"

    print(f"Тест пройден: данные сотрудника {employee_id} успешно обновлены.")