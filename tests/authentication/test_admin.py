from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestAdminSite(TestCase):

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

    def test_create_user_admin(self):
        """Teste para página de criação de usuário no admin"""
        url = reverse('admin:authentication_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_change_user_admin(self):
        """Teste para página de edição de usuário no admin"""
        url = reverse('admin:authentication_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_listed_users_admin(self):
        """Teste para página que lista os usuários"""
        url = reverse('admin:authentication_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.username)
