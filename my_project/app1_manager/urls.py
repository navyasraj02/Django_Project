from django.urls import path
from . import views

app_name = 'app1_manager'

urlpatterns = [
    path('simple-page/create/', views.create_post, name='post_create'),
    path('simple-page/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.posts, name='post_list')
]
