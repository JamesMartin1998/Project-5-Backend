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

    option1 = Count('votes', filter=Q(votes__option='option1'))
    option2 = Count('votes', filter=Q(votes__option='option2'))
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        option1_count=option1,
        option2_count=option2,
        comments_count=Count('comment', distinct=True)
    )

    # ordering filter allows posts to be sorted by number of votes or comments
    # they have DjangoFilterBackend allows posts to be sorted by category
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'votes_count',
        'comments_count'
    ]
    filterset_fields = [
        'category'
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
