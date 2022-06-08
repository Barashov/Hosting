from django.urls import path
from .views import UserCreateView, UsersView, UserProfileView


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup' ),
    path('users/', UsersView.as_view(), name='users'),
    path('user/<pk>/', UserProfileView.as_view(), name='user')
]
