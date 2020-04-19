from django.views.generic import TemplateView
from .models import Event


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = list(Event.objects.all().values())
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'