import pytest

from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_create_new_superuser(user_data):
  """ Teste para criação de super usuários. """
  user_model = get_user_model()
  assert user_model.objects.count() == 0
  admin_user = user_model.objects.create_superuser(**user_data)
  assert user_model.objects.count() == 1

@pytest.mark.django_db
def test_create_user_with_email(user_data):
  """ Teste para criar um novo usuário com o user model
        customizado (username, email, password) """
  user_model = get_user_model()
  user = user_model.objects.create_user(**user_data)
  assert user.email == 'admin@email.com'
  assert user.username == 'admin'
  assert user.check_password('12345678') == True

@pytest.mark.django_db
def test_change_user(client, user_create):
  """ Teste para edição de usuários. """
  user_model = get_user_model()
  user = user_model.objects.get(pk=user_create.id)
  assert user.email == 'admin@email.com'
  user_model.objects.update(email='admin_update@email.com', id=user.id)
  user_update = user_model.objects.get(pk=user_create.id)
  assert user_update.email == 'admin_update@email.com'