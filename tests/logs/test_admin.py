import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

from logs.models import Log

@pytest.mark.django_db
def test_create_log_admin(client, user_admin):
        """ Teste para view de criação de log no admin """
        url = reverse('admin:logs_log_add')
        response = client.get(url)

        assert response.status_code == 200

@pytest.mark.django_db
def test_change_log_admin(client, user_admin, log_create):
        """ Teste para view de edição de log no admin """
        url = reverse('admin:logs_log_change', args=[log_create.id])
        response = client.get(url)

        assert response.status_code == 200

@pytest.mark.django_db
def test_listed_log_admin(client, user_admin):
        """ Teste para view que lista os logs no admin """
        url = reverse('admin:logs_log_changelist')
        response = client.get(url)

        assert response.status_code == 200