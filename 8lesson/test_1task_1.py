import pytest
import requests
import uuid


BASE_URL = "https://yougile.com/api-v2"
BEARER_TOKEN = "xak98R2tvR7GUFpxVS77-0VlNtprJT80WsO3VTAR8Ro5TxCLcTUyPmxrYWVG4zIT"

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}


# Уникальное название проекта
def generate_unique_title():
    return f"TestProject-{uuid.uuid4()}"


def create_project():
    payload = {
        "title": generate_unique_title()
    }
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    assert response.status_code == 201, f"Setup failed: expected 201, got {response.status_code}"
    return response.json()["id"]


# Позитивный (Создание проекта) 
def test_create_project_success():
    payload = {
        "title": generate_unique_title()
    }

    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    assert "id" in data, "Response missing 'id'"
    assert isinstance(data["id"], str), "'id' is not a string"


# Негативный (Отсутствие  title)
def test_create_project_without_title():
    payload = {}

    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)

    assert response.status_code in [400, 422], f"Expected 400 or 422, got {response.status_code}"


# Позитивный (Изменение существующего проекта) 
def test_update_project_success():
    project_id = create_project()
    new_title = generate_unique_title()
    payload = {
        "title": new_title
    }

    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=payload, headers=HEADERS)

    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    # Проверим, что вернулся хотя бы ID
    data = response.json()
    assert "id" in data, "Response does not contain 'id'"
    assert data["id"] == project_id, "Returned ID doesn't match updated project"

    # Дополнительно проверим через GET
    get_response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert get_response.status_code == 200, f"GET failed with status {get_response.status_code}"
    project_data = get_response.json()
    assert project_data["title"] == new_title, f"Title not updated: expected {new_title}, got {project_data['title']}"


#  Негативный (Изменение несуществующего проекта)
def test_update_project_invalid_id():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    payload = {
        "title": "Нет проекта"
    }

    response = requests.put(f"{BASE_URL}/projects/{invalid_id}", json=payload, headers=HEADERS)

    assert response.status_code in [404, 400], f"Expected 404 or 400, got {response.status_code}"

# Получить проект по ID
def get_project_by_id(project_id):
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"Unexpected response: {response.status_code}, {response.text}")


# Позитивный (Получить существующий проект) 
def test_get_project_by_id_success():
    project_id = create_project()
    project = get_project_by_id(project_id)

    assert project is not None, "Project not found"
    assert project["id"] == project_id, "Returned project ID mismatch"
    assert "title" in project, "Missing title in response"
    assert isinstance(project["title"], str), "Title is not a string"

# Негативный (Получить несуществующий проект) 
def test_get_project_by_invalid_id():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    project = get_project_by_id(invalid_id)

    assert project is None, f"Expected no project, but got: {project}"
