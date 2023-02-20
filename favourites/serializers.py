# Code based from Code Institute's Django Rest Framework project
from django.db import IntegrityError
from rest_framework import serializers
from favourites.models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """
    sets the owner to the user's username as it's more readable
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourite
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Prevents users from adding a post as a favourite multiple times
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
