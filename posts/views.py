from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from lets_pick.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
from votes.models import Vote


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # queryset annotated to add extra fields that count the number of
    # total votes and specific types of votes on a post
    # https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#filtering-on-annotations

    option1 = Count('votes', filter=Q(votes__option='option1'), distinct=True)
    option2 = Count('votes', filter=Q(votes__option='option2'), distinct=True)
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        option1_count=option1,
        option2_count=option2,
        comments_count=Count('comment', distinct=True)
    )

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    # ordering filter allows posts to be sorted by number of votes or comments
    ordering_fields = [
        'votes_count',
        'comments_count'
    ]
    # DjangoFilterBackend - posts sorted by category, voted on by users,
    # favourited by users and owned by users
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    filterset_fields = [
        'category',
        'votes__owner__profile',
        'favourites__owner__profile',
        'author__profile'
    ]
    # search filter allows posts to be filtered by post title and author name
    search_fields = [
        'author__username',
        'title'
    ]

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
        option2_count=option2,
        comments_count=Count('comment', distinct=True)
    )
