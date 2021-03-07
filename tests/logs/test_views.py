import pytest

import requests
import json
from django.urls import reverse
from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.mark.django_db
def test_log_list_view(client, user_token):
  url = reverse('logs:logs-list')
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200

@pytest.mark.django_db
def test_log_create_view(client, user_token):
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
  url = reverse('logs:log-detail', args=[log_create.id])
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200
  assert response.data['id'] == log_create.id

@pytest.mark.django_db
def test_log_update_partial_view(client, user_token, log_create):
  # url = reverse('logs:log-detail', args=[log_create.id])
  url = "http://127.0.0.1:8000/api/v1/logs/"+str(log_create.id)
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImZvc2NoaWVyYWFuZGVyc29uQGdtYWlsLmNvbSIsImV4cCI6MTYxNTE5MTM0MiwiZW1haWwiOiJmb3NjaGllcmFhbmRlcnNvbkBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxNTAxODU0Mn0.nhz9nIC8Sn_chz3qorLrDEr97rPBiHf1ldwolSGU5pY"}
  data = {
    "title": "Log partial update",
    "description": "Descrição do Log partial update",
  }
  response = requests.patch(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 202
  assert response.json()['title'] == data['title']

@pytest.mark.django_db
def test_log_delete_view(client, user_token, log_create):
  url = reverse('logs:log-detail', args=[log_create.id])
  token = f"JWT {user_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.delete(url, headers=headers)
  assert response.status_code == 204