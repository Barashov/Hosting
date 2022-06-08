from .forms import CustomUserCreationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.


class UserCreateView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = '/'



class UsersView(ListView):
    model = UserProfile
    template_name = "users.html"
    context_object_name = 'users'
