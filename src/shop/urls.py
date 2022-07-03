from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="shop"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
]