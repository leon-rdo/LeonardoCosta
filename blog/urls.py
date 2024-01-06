from django.urls import path
from .views import BlogIndex

app_name = 'blog'
urlpatterns = [
    path('', BlogIndex.as_view(), name='blog_index'),
]