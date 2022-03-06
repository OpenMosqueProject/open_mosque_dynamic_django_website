from django.db import models
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=200)
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

