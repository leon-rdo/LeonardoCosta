from django.views.generic import FormView
from django.contrib import messages

from .models import *
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'home/index.html'
    form_class = ContactForm
    success_url = '/#contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Texts
        context["about_text"] = Text.objects.filter(spot='about').first()
        context["facts_text"] = Text.objects.filter(spot='facts').first()
        context["skills_text"] = Text.objects.filter(spot='skills').first()
        context["resume_text"] = Text.objects.filter(spot='resume').first()
        context["portfolio_text"] = Text.objects.filter(spot='portfolio').first()
        context["services_text"] = Text.objects.filter(spot='services').first()
        context["testimonial_texts"] = Text.objects.filter(spot='testimonials')
        context["contact_text"] = Text.objects.filter(spot='contact').first()
        # Formation
        context["formations"] = Education.objects.all()
        # Experience
        context["experiences"] = Experience.objects.all()
        # Skills
        context["skills"] = Skill.objects.all()
        # Portfolio
        context["portfolios"] = Portfolio.objects.all()
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Formulário enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Falha no envio do formulário. Por favor, verifique sua entrada.')
        return super().form_invalid(form)