from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="posts",)
    created_at = models.DateTimeField()


    def __str__(self):
        return f'{self.title}'
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    