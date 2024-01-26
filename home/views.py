from django.views.generic import TemplateView

from .models import *


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_text"] = Text.objects.filter(spot='about').first()
        context["facts_text"] = Text.objects.filter(spot='facts').first()
        context["skills_text"] = Text.objects.filter(spot='skills').first()
        context["resume_text"] = Text.objects.filter(spot='resume').first()
        context["portfolio_text"] = Text.objects.filter(spot='portfolio').first()
        context["services_text"] = Text.objects.filter(spot='services').first()
        context["testimonials_text"] = Text.objects.filter(spot='testimonials').first()
        context["contact_text"] = Text.objects.filter(spot='contact').first()
        return context
    