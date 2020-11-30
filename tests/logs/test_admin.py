from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from logs.models import Log


class TestAdminSite(TestCase):

    def setUp(self):
        self.client = Client()
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='12345678'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='teste',
            email='teste@email.com',
            password='12345678'
        )
        self.log = Log.objects.create(
            title='log',
            description='descrição para teste',
            level='DEBUG',
            origin='127.0.0.1',
            events=200,
            archived=False
        )

    def test_create_log_admin(self):
        """Teste para página de criação de log no admin"""
        url = reverse('admin:logs_log_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_change_log_admin(self):
        """Teste para página de edição de log no admin"""
        url = reverse('admin:logs_log_change', args=[self.log.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_listed_log_admin(self):
        """Teste para página que lista os logs"""
        url = reverse('admin:logs_log_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.log.title)