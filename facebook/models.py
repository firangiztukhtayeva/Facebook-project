from django.db import models

class Comment(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='comments/')
    text = models.TextField()
    created_at = models.DateTimeField()
