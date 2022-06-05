from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Sites
from django.views import View
from .logics import GetInformation
from .forms import CreateSiteForm


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


class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Sites
    template_name = "create_site.html"
    success_url = reverse_lazy("sites")
    form_class = CreateSiteForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
