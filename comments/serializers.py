# Code based from Code Institute's Django Rest Framework project
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Creates additional fields for the Comment model
    """
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        """
        check whether a user is the author of an object
        """
        request = self.context['request']
        return request.user == obj.author

    def get_created_at(self, obj):
        """
        use a more user friendly time format for created_at field
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        use a more user friendly time format for updated_at field
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'is_author', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')
