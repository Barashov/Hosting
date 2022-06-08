from django.urls import path
from .views import UserCreateView, UsersView


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup' ),
    path('users/', UsersView.as_view(), name='users'),
]
