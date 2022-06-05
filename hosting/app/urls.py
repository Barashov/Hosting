from django.urls import path
from .views import IndexView, SitesView, SiteView

urlpatterns = [
    path('', IndexView.as_view(), name='home' ),
    path("sites/", SitesView.as_view(), name="sites"),
    path("site/<pk>", SiteView.as_view(), name='site' )
]
