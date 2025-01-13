from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Services,SubService

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'main/html/index.html'

class AboutPageView(TemplateView):
    template_name = 'main/html/about.html'
