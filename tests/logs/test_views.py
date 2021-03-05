import pytest

import requests
from django.urls import reverse
from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.mark.django_db
def test_log_list_view(client, user_token):
  url = reverse('logs:logs-list')
  token = f"JWT {user_token.json()['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200

@pytest.mark.django_db
def test_log_create_view(client, user_token):
  url = reverse('logs:logs-list')
  token = f"JWT {user_token.json()['token']}"
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