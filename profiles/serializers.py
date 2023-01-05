from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # owner's username is more readable than id number
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name',
                        'content', 'image']
