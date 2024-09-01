from django.urls import path
from .views import BlogIndexView, PostCreateView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('publicacao/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('publicacao/nova/', PostCreateView.as_view(), name='post_create'),
]