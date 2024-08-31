from django.views.generic import ArchiveIndexView, CreateView, DetailView
from django.contrib import messages

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


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class PostCreateView(CreateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post salvo com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro ao salvar o post.')
        return super().form_invalid(form)