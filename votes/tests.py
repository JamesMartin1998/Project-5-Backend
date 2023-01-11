from django.contrib.auth.models import User
from .models import Vote
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class VoteListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='james', password='fakepassword')

    def test_can_list_votes(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        vote = Vote.objects.create(
            owner=james,
            post=post,
            option="option1"
        )
        response = self.client.get('/votes/')
        self.assertEqual(response.data[0]['option'], 'option1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_vote(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        self.client.login(username='james', password='fakepassword')
        response = self.client.post('/votes/', {
            'post': post.pk,
            'option': 'option1'
        })
        count = Vote.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_vote(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        response = self.client.post('/votes/', {
            'post': post.pk,
            'option': 'option1'
        })
        count = Vote.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class VoteDetailViewTests(APITestCase):
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
        Vote.objects.create(
            owner=james,
            post=post_by_james,
            option='option1'
        )

    def test_user_can_retrieve_vote_by_valid_id(self):
        response = self.client.get('/votes/1/')
        self.assertEqual(response.data['option'], 'option1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_vote_by_invalid_id(self):
        response = self.client.get('/votes/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_vote_if_owner(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put('/votes/1/', {
            'option': 'option2'
        })
        vote = Vote.objects.filter(pk=1).first()
        self.assertEqual(vote.option, 'option2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_vote_if_not_owner(self):
        self.client.login(username='aram', password='fakepassword')
        response = self.client.put('/votes/1/', {
            'option': 'option2'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_vote_if_owner(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.delete('/votes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_delete_vote_if_not_owner(self):
        self.client.login(username='aram', password='fakepassword')
        response = self.client.delete('/votes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
