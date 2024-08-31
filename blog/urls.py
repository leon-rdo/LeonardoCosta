from django.urls import path
from .views import BlogIndexView, PostCreateView

app_name = 'blog'
urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
]