from django.urls import path
from .views import UserCreateView, UsersView, UserProfileView, ProfileView, ProfileCreateView, ChangeProfileView


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup' ),
    path('users/', UsersView.as_view(), name='users'),
    path('user/<pk>/', UserProfileView.as_view(), name='user'),
    path('profile', ProfileView.as_view(), name='profile' ),
    path('create-profile', ProfileCreateView.as_view(), name='create_profile'),
    path('change-profile', ChangeProfileView.as_view(), name='change_profile')
]
