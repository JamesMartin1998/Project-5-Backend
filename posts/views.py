from django.db.models import Count
from rest_framework import generics, permissions, filters
from lets_pick.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
from votes.models import Vote


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        # option1_count=
        # option2_count=
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True)
    )
