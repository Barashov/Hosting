from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.


class UserCreateView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = '/'


