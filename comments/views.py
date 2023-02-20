# Code based from Code Institute's Django Rest Framework project
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from lets_pick.permissions import IsAuthorOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    All users can list comments. Logged in users can create comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        """
        Associates comments with a user when created
        """
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Users can read a comment, author can edit and delete their comment
    """
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
