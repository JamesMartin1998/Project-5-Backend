from django.contrib.auth.models import User
from .models import Favourite
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class FavouriteListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='james', password='fakepassword')

    def test_can_list_favourites(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        favourite = Favourite.objects.create(
            owner=james,
            post=post,
        )
        response = self.client.get('/favourites/')
        self.assertEqual(response.data[0]['owner'], 'james')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_favourite(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        self.client.login(username='james', password='fakepassword')
        response = self.client.post('/favourites/', {
            'post': post.pk,
        })
        count = Favourite.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_favourite(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        response = self.client.post('/favourites/', {
            'post': post.pk,
        })
        count = Favourite.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FavouriteDetailViewTests(APITestCase):
    def setUp(self):
        james = User.objects.create_user(
            username='james',
            password="fakepassword"
        )
        aram = User.objects.create_user(
            username='aram',
            password='fakepassword'
        )
        post_by_james = Post.objects.create(
            author=james,
            title='test',
            category="sport"
        )
        favourite = Favourite.objects.create(
            owner=james,
            post=post_by_james
        )

    def test_user_can_retrieve_favourite_by_valid_id(self):
        response = self.client.get('/favourites/1/')
        self.assertEqual(response.data['owner'], 'james')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_favourite_by_invalid_id(self):
        response = self.client.get('/favourites/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_favourite_if_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.delete('/favourites/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_delete_favourite_if_not_author(self):
        self.client.login(username='aram', password='fakepassword')
        response = self.client.delete('/favourites/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
