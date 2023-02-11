
from django.urls import path
from . import views

app_name = 'app1_manager'

urlpatterns = [
    path('create/', views.create_post, name='post_create'),
    path('', views.posts, name='post_list'),
]