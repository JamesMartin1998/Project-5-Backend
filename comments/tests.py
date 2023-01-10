from django.contrib.auth.models import User
from .models import Comment
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='james', password='fakepassword')

    def test_can_list_comments(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        comment = Comment.objects.create(
            author=james,
            post=post,
            content="Test Comment"
        )
        response = self.client.get('/comments/')
        self.assertEqual(response.data[0]['content'], 'Test Comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_comment(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        self.client.login(username='james', password='fakepassword')
        response = self.client.post('/comments/', {
            'post': post.pk,
            'content': 'Test Comment'
        })
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_comment(self):
        james = User.objects.get(username='james')
        post = Post.objects.create(author=james, title="Test Post")
        response = self.client.post('/comments/', {
            'post': post.pk,
            'content': 'Test Comment'
        })
        count = Comment.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
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
        Comment.objects.create(
            author=james,
            post=post_by_james,
            content="Test Comment"
        )

    def test_user_can_retrieve_comment_by_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'Test Comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_comment_by_invalid_id(self):
        response = self.client.get('/comments/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_comment_if_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put('/comments/1/', {
            'content': 'Updated content'
        })
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'Updated content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_comment_if_not_author(self):
        self.client.login(username='aram', password='fakepassword')
        response = self.client.put('/comments/1/', {
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_comment_if_author(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_delete_comment_if_not_author(self):
        self.client.login(username='aram', password='fakepassword')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
