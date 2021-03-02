import pytest

from django.urls import reverse

from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_create_user_admin_view(client, user_admin):
  """ Teste na view de criação de usuário no admin. """
  url = reverse('admin:authentication_user_add')
  response = client.get(url)
  assert response.status_code == 200

@pytest.mark.django_db
def test_change_user_admin_view(client, user_admin):
  """ Teste na view de edição de usuário no admin. """
  url = reverse('admin:authentication_user_change', args=[user_admin.id])
  response = client.get(url)
  assert response.status_code == 200

@pytest.mark.django_db
def test_listed_user_admin_view(client, user_admin):
  """ Teste na view de listagem de usuários no admin. """
  url = reverse('admin:authentication_user_changelist')
  response = client.get(url)
  assert response.status_code == 200