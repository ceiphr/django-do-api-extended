from django.views.generic import TemplateView
from .services import get_all_droplets, get_droplet


class GetAllDroplets(TemplateView):
    template_name = 'all_droplets.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'droplets': get_all_droplets(),
        }
        return context


class GetDroplet(TemplateView):
    template_name = 'droplet.html'

    def get_context_data(self, droplet, *args, **kwargs):
        context = {
            'droplet': get_droplet(droplet),
        }
        return context

