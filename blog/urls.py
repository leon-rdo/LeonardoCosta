from django.urls import path
from .views import BlogIndexView, PostCreateView, PostDetailView, PostUpdateView, delete_post, switch_published

app_name = 'blog'
urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('publicacao/nova/', PostCreateView.as_view(), name='post_create'),
    path('publicacao/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('publicacao/<slug:slug>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('publicacao/<int:pk>/excluir/', delete_post, name='post_delete'),
    path('publicacao/<int:pk>/publicar/', switch_published, name='post_switch_published'),
]