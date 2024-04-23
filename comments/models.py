from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

