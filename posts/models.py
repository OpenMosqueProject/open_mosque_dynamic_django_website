from django.db import models
from django.urls import reverse
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os

# Create your models here.
POST_CHOICES = [
    ('News', 'News'),
    ('Events', 'Events'),
    
]

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000) # RichTextField()
    type = models.CharField(max_length=200, choices=POST_CHOICES)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFill(800, 450)],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        """Returns the image URL or falls back to default static image"""
        if self.image:
            return self.image.url
        return os.path.join(settings.STATIC_URL, 'images/default_image.jpg')

    def get_absolute_url(self, id=id or None):
        return reverse("posts:post_view", kwargs={'id':self.id})
