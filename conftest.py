import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.fixture
def user_data():
    """ Retorna um usuário """
    return {
        'username': 'admin',
        'email': 'admin@email.com',
        'password': '12345678'
    }

@pytest.fixture
def user_create(user_data):
    """ Cria um usuário no banco de dados e retorna o objeto criado """
    user_model = get_user_model()
    user = user_model.objects.create_user(**user_data)
    return user

@pytest.fixture
def log_data():
    """ Retorna um log """
    return {
        'title': 'log',
        'description': 'descrição para teste',
        'level': 'DEBUG',
        'origin': '127.0.0.1',
        'events': 200,
        'archived': False
    }

@pytest.fixture
def user_admin(client, user_data):
    """ Retorna um usuário autenticado """
    user_model = get_user_model()
    user_admin = user_model.objects.create_superuser(**user_data)
    client.force_login(user_admin)
    return user_admin

@pytest.fixture
def log_create(log_data):
    """ Cria um log no banco de dados e retorna o objeto criado """
    log = Log.objects.create(**log_data)
    return log

@pytest.fixture
def user_token(client, user_create):
    url = reverse('authentication:obtain_token')
    client.force_login(user_create)
    user_token = client.post(url, {"email": "admin@email.com", "password": "12345678"})
    return user_token

@pytest.fixture
def superuser_token(client, user_admin):
    url = reverse('authentication:obtain_token')
    client.force_login(user_admin)
    superuser_token = client.post(url, {"email": "admin@email.com", "password": "12345678"})
    return superuser_token