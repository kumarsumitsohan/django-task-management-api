from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task

User = get_user_model()


class AuthTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'StrongPass123!',
            'password2': 'StrongPass123!',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='alice').exists())

    def test_register_password_mismatch(self):
        url = reverse('register')
        data = {
            'username': 'bob',
            'password': 'StrongPass123!',
            'password2': 'Different123!',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_returns_tokens(self):
        User.objects.create_user(username='carol', password='StrongPass123!')
        url = reverse('token_obtain_pair')
        response = self.client.post(
            url, {'username': 'carol', 'password': 'StrongPass123!'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class TaskCRUDTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='dave', password='pass12345')
        self.other = User.objects.create_user(username='erin', password='pass12345')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Write report', 'status': 'pending', 'priority': 'high'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get().owner, self.user)

    def test_list_tasks_only_shows_own(self):
        Task.objects.create(owner=self.user, title='Mine')
        Task.objects.create(owner=self.other, title='Not mine')
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Mine')

    def test_retrieve_others_task_forbidden(self):
        task = Task.objects.create(owner=self.other, title='Not mine')
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url)
        self.assertIn(
            response.status_code,
            (status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND),
        )

    def test_update_task(self):
        task = Task.objects.create(owner=self.user, title='Old title')
        url = reverse('task-detail', args=[task.id])
        response = self.client.patch(url, {'title': 'New title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'New title')

    def test_delete_task(self):
        task = Task.objects.create(owner=self.user, title='Delete me')
        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_filter_by_status(self):
        Task.objects.create(owner=self.user, title='A', status='pending')
        Task.objects.create(owner=self.user, title='B', status='completed')
        url = reverse('task-list') + '?status=completed'
        response = self.client.get(url)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'B')

    def test_unauthenticated_request_denied(self):
        self.client.force_authenticate(user=None)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
