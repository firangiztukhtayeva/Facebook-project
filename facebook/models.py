from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_image/')
    text = models.TextField()
    created_at = models.DateTimeField()
