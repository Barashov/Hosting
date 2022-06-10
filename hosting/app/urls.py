from django.urls import path
from .views import IndexView, SitesView, SiteView, SiteCreateView, GetUserSitesListView

urlpatterns = [
    path('', IndexView.as_view(), name='home' ),
    path("sites/", SitesView.as_view(), name="sites"),
    path("site/<pk>", SiteView.as_view(), name='site'),
    path("create_site/", SiteCreateView.as_view(), name="create_site"),
    path("user-sites", GetUserSitesListView.as_view(), name="user_sites"),
]
