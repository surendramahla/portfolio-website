from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Skill, Project, Experience
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class SkillsView(ListView):
    model = Skill
    template_name = 'core/skills.html'
    context_object_name = 'skills'

class ProjectsView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'

class ExperienceView(ListView):
    model = Experience
    template_name = 'core/experience.html'
    context_object_name = 'experiences'

class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)
