from django.contrib import admin
#from solo.admin import SingletonModelAdmin
from .models import CentreProfile

# Register your models here.

admin.site.register(CentreProfile) #, SingletonModelAdmin