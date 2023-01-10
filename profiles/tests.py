from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        james = User.objects.create(username='james', password='fakepassword')

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.data[0]['owner'], 'james')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        james = User.objects.create_user(
            username='james',
            password="fakepassword"
        )
        aram = User.objects.create_user(
            username='aram',
            password='fakepassword'
        )

    def test_user_can_retrieve_profile_by_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'james')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_profile_if_owner(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put('/profiles/1/', {
            'owner': 'james',
            'name': "james' profile",
            'description': 'This is my profile'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, "james' profile")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_profile_if_not_owner(self):
        self.client.login(username='james', password='fakepassword')
        response = self.client.put('/profiles/2/', {
            'owner': 'aram',
            'name': 'noupdate',
            'description': 'noupdate'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
