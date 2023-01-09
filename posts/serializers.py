from rest_framework import serializers
from .models import Post


class PostSerializer(models.Model):
    author = models.ReadOnlyField(source="author.username")
    is_author = models.SerializerMethodField()
    profile_id = models.ReadOnlyField(source="author.profile.id")
    profile_image = models.ReadOnlyField(source="author.profile.image.id")

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

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'category', 'image'
        ]
