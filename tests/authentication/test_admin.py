from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from logs.models import Log


class AdminSiteTests(TestCase):

    def setUp(self):
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
            description='descricao para teste',
            level='DEBUG',
            origin='127.0.0.1',
            events=200,
            archived=False
        )

    def test_users_listed(self):
        """Teste para saber se os usuário estão sendo
        listados na página de admin"""
        url = reverse('admin:authentication_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Teste de edição dos dados do usuário no admin"""
        url = reverse('admin:authentication_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Teste de criação de um novo usuário no admin"""
        url = reverse('admin:authentication_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_logs_listed(self):
        """Teste de listagem dos logs no admin"""
        url = reverse('admin:logs_log_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_log_change_page(self):
        """Teste de edição dos logs no admin"""
        url = reverse('admin:logs_log_change', args=[self.log.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_log_page(self):
        """Teste de criação de um novo log no admin"""
        url = reverse('admin:logs_log_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)