from rest_framework import serializers
from .models import Post


class PostSerializer(models.Model):
    author = models.ReadOnlyField(source="author.username")
    is_author = models.SerializerMethodField()
    profile_id = models.ReadOnlyField(source="author.profile.id")
    profile_image = models.ReadOnlyField(source="author.profile.image.id")

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'category', 'image'
        ]
