from rest_framework import serializers
from .models import Post
from favourites.models import Favourite
from votes.models import Vote


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="author.profile.id")
    profile_image = serializers.ReadOnlyField(source="author.profile.image.id")
    favourite_id = serializers.SerializerMethodField()
    vote_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()
    option1_count = serializers.ReadOnlyField()
    option2_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        """
        Checks if the current user is the author of the post
        """
        request = self.context['request']
        return request.user == obj.author

    # validate_image function used from Code Institute's Moments Project
    def validate_image(self, value):
        """
        Validates the post image so that images that are too large can't be
        uploaded
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    # get_favourite_id function adapts on Code Institute's Moments Project
    def get_favourite_id(self, obj):
        """
        Returns Favourite id if a user is logged in and has favourited the post
        Else, returns None
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, post=obj
            ).first()
            return favourite.id if favourite else None
        None

    def get_vote_id(self, obj):
        """
        Returns Vote id if a user is logged in and has voted on the post
        Else, returns None
        """
        user = self.context['request'].user
        if user.is_authenticated:
            vote = Vote.objects.filter(
                owner=user, post=obj
            ).first()
            return vote.id if vote else None
        None

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'category', 'image', 'favourite_id',
            'vote_id', 'votes_count', 'option1_count', 'option2_count'
        ]
