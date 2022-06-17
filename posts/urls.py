from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('monthly_times/', views.month_view, name='month_view'),
    path('post/<int:id>', views.post_view, name='post_view'),
]
