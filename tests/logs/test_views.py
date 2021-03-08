import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.mark.django_db
def test_log_list_view(client, user_token):
  """ Teste na view de listagem dos logs """
  url = reverse('logs:logs-list')
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200

@pytest.mark.django_db
def test_log_create_view(client, user_token):
  """ Teste na view de criação de um log """
  url = reverse('logs:logs-list')
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  data = {
    "title": "Log",
    "description": "Descrição do log",
    "origin": "127.0.0.1",
    "level": "Warning",
    "events": 743,
    "archived": False
  }
  response = client.post(url, data=data, headers=headers)
  assert response.status_code == 201
  assert 'title' in response.json()

@pytest.mark.django_db
def test_log_detail_view(client, user_token, log_create):
  """ Teste na view de listagem de um único log """
  url = reverse('logs:log-detail', args=[log_create.id])
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200
  assert response.data['id'] == log_create.id

@pytest.mark.django_db
def test_log_delete_view(client, user_token, log_create):
  """ Teste na view para deletar um log """
  url = reverse('logs:log-detail', args=[log_create.id])
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.delete(url, headers=headers)
  assert response.status_code == 204