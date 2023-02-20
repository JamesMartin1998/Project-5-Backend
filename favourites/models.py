# Code based from Code Institute's Django Rest Framework project
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favourite(models.Model):
    """
    Favourite model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='favourites', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'Favourite {self.owner} on {self.post}'
