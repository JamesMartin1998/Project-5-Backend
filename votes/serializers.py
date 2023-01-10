from rest_framework import serializers
from votes.models import Vote


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = ['id', 'created_at', 'owner', 'post']