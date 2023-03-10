# Code based from Code Institute's Django Rest Framework project
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    Image from Code Institute's Django Rest Framework project
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-profile-image_i9e1dj'
    )

    class Meta:
        # returns profiles by newest created first
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile automatically when a new user is created
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
