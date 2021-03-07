import pytest

from django.shortcuts import reverse
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_login_admin_view(client):
  """ Teste na view de login de usuário pelo admin """
  url = reverse('admin:login')
  response = client.get(url)
  assert response.status_code == 200

@pytest.mark.django_db
def test_check_user_not_authenticated_admin(client):
  """ Teste para checar se o usuário não está autenticado no admin """
  url = reverse('admin:index')
  response = client.get(url)
  assert response.status_code != 200

@pytest.mark.django_db
def test_check_user_is_authenticated_admin(client, user_admin):
  """ Teste para checar se o usuário está autenticado no admin """
  url = reverse('admin:index')
  response = client.get(url)
  assert response.status_code == 200