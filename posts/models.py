from django.db import models
from django.urls import reverse
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

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
    image = VersatileImageField('Image', upload_to='images/', 
            blank=True,
            placeholder_image=OnStoragePlaceholderImage(
                path='images/default_image.jpg'
        ))

    def __str__(self):
        return self.title

    def get_absolute_url(self, id=id or None):
        return reverse("posts:post_view", kwargs={'id':self.id})
