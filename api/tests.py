from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import BlogModel


# Create your tests here.
class CHeckStatusTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_check_status(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestBlogs(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        BlogModel.objects.create(user, title='salam', description='This is usually ', date='2023-11-22')
        BlogModel.objects.create(user, title='hello', description='This is salam', date='2023-11-22')

    def test_title(self):
        chart1 = BlogModel.objects.get(title='salam')
        chart2 = BlogModel.objects.get(title='hola')
        self.assertEqual(chart1.title, 'salam')
        self.assertNotEqual(chart2.title, 'hola')
