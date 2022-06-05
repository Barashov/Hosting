from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Sites
from django.views import View
from .logics import GetInformation

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"
    
    
class SitesView(ListView):
    model = Sites
    template_name = "sites.html"
    context_object_name = "sites"

class SiteView(View):
    def get(self, request, pk):
        file_name = str(GetInformation.get_file_name(pk))
        return render(request, file_name)

