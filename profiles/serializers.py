# Code based from Code Institute's Django Rest Framework project
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Add more fields to the Profile model
    owner's username is more readable than id number
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    votes_made = serializers.ReadOnlyField()
    votes_received = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        checks if object is owned by a user
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name',
                        'description', 'image', 'is_owner',
                        'posts_count', 'votes_made', 'votes_received']
