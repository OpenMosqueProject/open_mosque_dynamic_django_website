from django.urls import path, include

from . import views
from .views import get_month_tbl
app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('monthly_times/', views.month_view, name='month_view'),
    path('post/<int:id>/', views.post_view, name='post_view'),
    path('posts-admin', views.posts_admin, name='posts_admin'),
    path('posts', views.post_list_view, name='post_list'),
    path('create_post', views.post_form, name='post_form'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:id>/toggle', views.hide_post_toggle, name='post_toggle'),
    path('post/edit/<int:id>/', views.edit_post_form, name='post_edit'),
    path('pdf', views.GeneratePdf.as_view(), name="pdf"),
]
