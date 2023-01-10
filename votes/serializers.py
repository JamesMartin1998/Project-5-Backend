from django.db import IntegrityError
from rest_framework import serializers
from votes.models import Vote


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = ['id', 'created_at', 'owner', 'post']

    # create method used from Code Institute's Moments Project
    # https://github.com/Code-Institute-Solutions/drf-api/blob/a918da6065ef5c399ff7655638960c2628af83d4/likes/serializers.py
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
