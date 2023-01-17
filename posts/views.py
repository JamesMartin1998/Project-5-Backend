from django.db.models import Count, Q
from rest_framework import generics, permissions, filters
from lets_pick.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
from votes.models import Vote


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    option1 = Count('votes', filter=Q(votes__option='option1'))
    option2 = Count('votes', filter=Q(votes__option='option2'))
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        option1_count=option1,
        option2_count=option2
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    option1 = Count('votes', filter=Q(votes__option='option1'))
    option2 = Count('votes', filter=Q(votes__option='option2'))
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        option1_count=option1,
        option2_count=option2
    )
