import pytest

import requests
from django.urls import reverse
from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.mark.django_db
def test_log_create_view(client, user_token, log_data):
  url = "http://127.0.0.1:8000/api/v1/logs/"
  headers = {"Content-Type": "application/json", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6InRlc3RlMkB0ZXN0ZS5jb20iLCJleHAiOjE2MTQ5ODQ2ODcsImVtYWlsIjoidGVzdGUyQHRlc3RlLmNvbSIsIm9yaWdfaWF0IjoxNjE0ODExODg3fQ.-84beTlkx3-dUGkF4Exqx8npYgIJtnSJLSNTcBf6dRE"}
  data = {"title": "Log 6","description": "Descrição do Log 2","origin": "127.0.0.1","level": "Warning","events": 743903,"archived": False}
  response = requests.post(url, json=data, headers=headers)
  assert response.status_code == 201
  assert 'title' in response.json()