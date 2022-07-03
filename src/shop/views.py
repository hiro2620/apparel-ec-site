from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class TopView(TemplateView):
    template_name = "shop/top.html"

class HomeView(LoginRequiredMixin, ListView):
    template_name = "shop/home.html"