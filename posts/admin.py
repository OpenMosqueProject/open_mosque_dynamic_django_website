from django.contrib import admin
from .models import Post

from solo.admin import SingletonModelAdmin
from .models import CentreProfile

# Register your models here.
admin.site.register(Post)
admin.site.register(CentreProfile, SingletonModelAdmin)