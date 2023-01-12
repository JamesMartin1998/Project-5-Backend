from django.db.models import Count
from rest_framework import generics, filters
from lets_pick.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    # queryset = Profile.objects.annotate(
    #     posts_count=Count('owner__post', distinct=True),
    #     votes_made=Count('owner__vote', distinct=True),
    #     # votes_received=Count("owner__post__votes", distinct=True)
    # )
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
