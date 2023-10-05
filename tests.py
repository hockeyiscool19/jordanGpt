import pytest
from run import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Welcome! With this API, you can access my resume data.' in response.data


def test_get_skills(client):
    response = client.get('/resume/skills')
    assert response.status_code == 200


def test_get_work_experience(client):
    response = client.get('/resume/work_experience')
    assert response.status_code == 200


def test_get_internship_no_name(client):
    response = client.get('/resume/internships')
    assert response.status_code == 200
    assert b'Please provide an internship name' in response.data


def test_get_projects(client):
    response = client.get('/resume/projects')
    assert response.status_code == 200


def test_get_education(client):
    response = client.get('/resume/education')
    assert response.status_code == 200


def test_get_role_description_datashapes(client):
    response = client.get('/roleDescriptions/datashapes')
    assert response.status_code == 200


def test_get_contact_info(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Jordan Eisenman' in response.data
    assert b'jordaneisenman@gmail.com' in response.data
    assert b'802-733-7703' in response.data


def test_jordan_gpt_with_question(client):
    data = {"question": "Tell me about Jordan's four internships?"}
    response = client.get('/jordan_gpt', json=data)

    # Check that the status code is 200 (OK)
    assert response.status_code == 200
