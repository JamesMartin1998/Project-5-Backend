from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

option_choices = [
    ('option1', 'Option 1'), ('option2', 'Option 2')
]


class Vote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name="votes",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    option = models.CharField(choices=option_choices, max_length=30)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{option} vote by {self.owner} on {self.post}'
