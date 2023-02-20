# Code based from Code Institute's Django Rest Framework project
from rest_framework import generics, permissions
from lets_pick.permissions import IsOwnerOrReadOnly
from favourites.models import Favourite
from favourites.serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    """
    All users can list favourites. Logged in users can create favourites
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        """
        Associates favourites with a user when created
        """
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Users can read a favourite, owner can edit and delete their favourite
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
