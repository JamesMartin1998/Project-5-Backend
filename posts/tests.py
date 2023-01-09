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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        james = User.objects.create_user(
            username='james',
            password="fakepassword"
        )
        aram = User.objects.create_user(
            username='aram',
            password='fakepassword'
        )
        Post.objects.create(
            author=james,
            title='test',
            category="sport"
        )
        Post.objects.create(
            author=aram,
            title='test2',
            category="people"
        )

    def test_user_can_retrieve_post_by_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_post_by_invalid_id(self):
        response = self.client.get('/posts/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_post_if_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put(
            '/posts/1/',
            {'title': 'testupdated', 'category': 'people'}
        )
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'testupdated')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_post_if_not_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put(
            '/posts/2/',
            {'title': 'testupdated', 'category': 'people'}
        )
        post = Post.objects.filter(pk=2).first()
        # self.assertEqual(post.title, 'testupdated')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_post_if_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.delete(
            '/posts/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_post_if_not_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.delete(
            '/posts/2/'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
