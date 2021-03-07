import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

def test_unauthorized_render_view(client):
  url = reverse('authentication:users-list')
  response = client.get(url)
  assert response.status_code == 401

@pytest.mark.django_db
def test_authorized_render_view(client, user_admin):
  url = reverse('authentication:users-list')
  response = client.get(url)
  assert response.status_code == 200

@pytest.mark.django_db
def test_user_register_view(client, user_data):
  url = reverse('authentication:register')
  response = client.post(url, data=user_data)
  assert response.status_code == 201

@pytest.mark.django_db
def test_user_create_token_view(client, user_data):
  user = get_user_model().objects.create_user(**user_data)
  assert user.email == 'admin@email.com'
  url = reverse('authentication:obtain_token')
  data = {"email": f"{user_data['email']}", "password": f"{user_data['password']}"}
  response = client.post(url, data)
  assert response.status_code == 200
  assert 'token' in response.data

@pytest.mark.django_db
def test_user_list_view(client, superuser_token):
  url = reverse('authentication:users-list')
  token = f"JWT {superuser_token.data['token']}"
  headers = {"Content-Type": "application/json", "Authorization": token}
  response = client.get(url, headers=headers)
  assert response.status_code == 200