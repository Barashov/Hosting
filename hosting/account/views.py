
from django.shortcuts import redirect, render


from django.views import View
from .forms import CustomUserCreationForm, ProfileForm
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
        profile = GetInformation.get_file(pk)
        return render(request, 'user_profile.html', {'profile': profile})
    
class ProfileView(View):
    def get(self, request):
        if GetInformation.is_have_profile(request.user):
            profile = GetInformation.get_profile(request.user)
            return render(request, 'user_profile.html', {'profile': profile})
        else:
            return redirect('create_profile')

class ProfileCreateView(CreateView):
    model = UserProfile
    template_name = "create_profile.html"
    success_url = '/'
    form_class = ProfileForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)