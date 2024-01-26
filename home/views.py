from django.views.generic import TemplateView

from .models import *


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_text"] = Text.objects.filter(spot='about').first()
        return context
    