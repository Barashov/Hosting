from django.shortcuts import render
from django.views import View
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .models import UserProfile
from .logic import GetInformation
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

class UserProfileView(View):
    def get(self, request, pk):
        profile = GetInformation.get_user_profile(pk)
        return render(request, 'user_profile.html', {'profile': profile})