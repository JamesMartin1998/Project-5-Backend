# Code based from Code Institute's Django Rest Framework project
from django.db import models
from django.contrib.auth.models import User

category_choices = [
    ('sport', 'Sport'), ('people', 'People'), ('places', 'Places'),
    ('food', 'Food'), ('entertainment', 'Entertainment'),
    ('fashion', 'Fashion'), ('animals', 'Animals'), ('other', 'Other')
]


class Post(models.Model):
    """
    Post model. category field allows options from the category_choices list
    default image from Code Institute's Django Rest Framework project
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.CharField(choices=category_choices, max_length=30)
    image = models.ImageField(
        upload_to="images/", default="../default-post-image_wnd0vc", blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title} by {self.author}'
