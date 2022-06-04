from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Sites
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"
    
    
class SitesView(ListView):
    model = Sites
    template_name = "sites.html"
    context_object_name = "sites"

