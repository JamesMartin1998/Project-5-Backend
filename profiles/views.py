# Code based from Code Institute's Django Rest Framework project
from django.db.models import Count
from rest_framework import generics, filters
from lets_pick.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Users can list profiles
    """
    # queryset annotated to add extra fields that count the number of posts
    # made, votes made and votes received by a user
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        votes_made=Count('owner__vote', distinct=True),
        votes_received=Count("owner__post__votes", distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    # ordering filter allows posts to be sorted by number of oosts made, votes
    # made or votes received
    ordering_fields = [
        'posts_count',
        'votes_made',
        'votes_received'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Users can read profiles, owners can edit their profiles
    """
    permission_classes = [IsOwnerOrReadOnly]
    # queryset annotated to add extra fields that count the number of posts
    # made, votes made and votes received by a user
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        votes_made=Count('owner__vote', distinct=True),
        votes_received=Count("owner__post__votes", distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
