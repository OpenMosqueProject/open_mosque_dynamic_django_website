from django.urls import path, include

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('monthly_times/', views.month_view, name='month_view'),
    path('post/<int:id>', views.post_view, name='post_view'),
    #path('edit-post/<int:id>', views.edit_post, name='edit_post'),
    path('posts-admin', views.posts_admin, name='posts_admin'),
    path('posts', views.post_list_view, name='post_list'),
    path('create_post', views.post_form, name='post_form'),
]
