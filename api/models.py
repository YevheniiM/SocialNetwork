from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    """
    User profile model.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=255, blank=True, null=True)
    biography = models.TextField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Post(models.Model):
    """
    Post which is always made by user.

    """
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """
    Like model, always made at a concrete post.

    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # to be sure that one user will not add the like to the same
        # post more than one time
        unique_together = ['post', 'made_by']


class Comment(models.Model):
    """
    Comment model, always made at a concrete post.

    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=2047)
