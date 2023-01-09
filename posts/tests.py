from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='james', password="fakepassword")

    def test_can_list_posts(self):
        james = User.objects.get(username='james')
        Post.objects.create(author=james, title="test post")
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.post('/posts/', {
            'title': 'a title',
            'category': 'sport'
        })
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {
            'title': 'a title',
            'category': 'sport'
        })
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
