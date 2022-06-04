from django.urls import path
from .views import IndexView, SitesView

urlpatterns = [
    path('', IndexView.as_view(), name='home' ),
    path("sites/", SitesView.as_view(), name="sites"),
]
