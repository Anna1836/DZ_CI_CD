import pytest
import requests

# Базовые адреса сервисов
BASE_GET_URL = 'https://postman-echo.com/get'
BASE_POST_URL = 'https://postman-echo.com/post'

@pytest.fixture(scope='session')
def session():
    """Фикстура для создания сеанса"""
    return requests.Session()

# Тест №1: Простой GET-запрос
def test_simple_get(session):
    """Проверка базового GET-запроса."""
    response = session.get(BASE_GET_URL)
    assert response.status_code == 200
    assert not response.json().get('args'), 'Параметры args не пусты'

# Тест №2: GET-запрос с параметрами
def test_get_with_query_params(session):
    """Проверка GET-запроса с параметрами."""
    params = {'foo': 'bar'}
    response = session.get(BASE_GET_URL, params=params)
    assert response.status_code == 200
    assert response.json().get('args') == params, 'Полученные аргументы не совпадают'

# Тест №3: Простой POST-запрос с JSON-телом
def test_post_json_body(session):
    """Проверка POST-запроса с JSON-телом."""
    payload = {"hello": "world"}
    headers = {'Content-Type': 'application/json'}
    response = session.post(BASE_POST_URL, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json().get('json') == payload, 'JSON в ответе отличается от отправленного'

# Тест №4: POST-запрос с формами данных
def test_post_form_data(session):
    """Проверка POST-запроса с формой данных."""
    form_data = {'foo': 'bar'}
    response = session.post(BASE_POST_URL, data=form_data)
    assert response.status_code == 200
    assert response.json().get('form') == form_data, 'Форма в ответе отличается от отправленной'

# Тест №5: HEAD-запрос для проверки заголовков
def test_head_request(session):
    """Проверка наличия заголовка Server в ответе на HEAD-запрос."""
    response = session.head(BASE_GET_URL)
    assert response.status_code == 200
    expected_headers = ['Server']
    for header in expected_headers:
        assert header.lower() in map(str.lower, response.headers.keys()), f'Заголовок "{header}" не найден'
