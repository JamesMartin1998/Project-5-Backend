from django.db.models import Count
from rest_framework import generics, filters
from lets_pick.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        votes_made=Count('owner__vote', distinct=True),
        votes_received=Count("owner__post__votes", distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'votes_made',
        'votes_received'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        votes_made=Count('owner__vote', distinct=True),
        votes_received=Count("owner__post__votes", distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
