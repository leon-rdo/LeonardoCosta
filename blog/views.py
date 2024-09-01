from django.contrib import messages
from django.views.generic import ArchiveIndexView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from blog.forms import PostForm
from .models import Post


class BlogIndexView(ArchiveIndexView):
    template_name = 'blog/index.html'
    date_field = 'published_at'
    allow_empty = True
    allow_future = True
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['-published_at']
    model = Post
    make_object_list = True

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class PostDetailView(UserPassesTestMixin, DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def test_func(self):
        return self.get_object().is_published or self.request.user.has_perm('blog.view_post')


class PostCreateView(UserPassesTestMixin, CreateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostForm
    success_url = '/blog/'

    def test_func(self):
        return self.request.user.has_perm('blog.add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post salvo com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro ao salvar o post.')
        return super().form_invalid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostForm
    success_url = '/blog/'

    def test_func(self):
        return self.request.user.has_perm('blog.change_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post salvo com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro ao salvar o post.')
        return super().form_invalid(form)