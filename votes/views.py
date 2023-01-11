from rest_framework import generics, permissions
from lets_pick.permissions import IsOwnerOrReadOnly
from .models import Vote
from .serializers import VoteSerializer, VoteDetailSerializer


class VoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        """
        Associates votes with a user when created
        """
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteDetailSerializer
    queryset = Vote.objects.all()
