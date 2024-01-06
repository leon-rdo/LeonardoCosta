from django.views.generic import TemplateView


class BlogIndex(TemplateView):
    template_name = 'blog/index.html'


'''
from django.views.generic.dates import ArchiveIndexView


class BlogIndexView(ArchiveIndexView):
    template_name = 'blog/index.html'
    date_field = 'date'
    allow_empty = True
    allow_future = True
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['-date']
    context_object_name = 'posts'
    model = Post
    make_object_list = True
'''