# Code based from Code Institute's Django Rest Framework project
from django.db import IntegrityError
from rest_framework import serializers
from votes.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    username more readable for user
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = ['id', 'created_at', 'owner', 'post', 'option']

    def create(self, validated_data):
        """
        Prevents users from voting multiple times on a post
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


class VoteDetailSerializer(VoteSerializer):
    """
    Users can move the vote instance to another post
    """
    post = serializers.ReadOnlyField(source='post.id')
