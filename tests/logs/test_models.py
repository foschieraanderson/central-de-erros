import pytest

from django.contrib.auth import get_user_model

from logs.models import Log

@pytest.mark.django_db
def test_create_new_log(log_data):
  """ Teste para criação de logs. """
  assert Log.objects.count() == 0
  log = Log.objects.create(**log_data)
  assert Log.objects.count() == 1

@pytest.mark.django_db
def test_change_log(client, log_create):
  """ Teste para edição de logs. """
  log = Log.objects.get(pk=log_create.id)
  assert log.title == 'Log'
  Log.objects.update(title='Log Update', id=log.id)
  log_update = Log.objects.get(pk=log_create.id)
  assert log_update.title == 'Log Update'