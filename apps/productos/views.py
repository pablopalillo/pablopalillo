from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
from .models import Producto

class index(ListView):
    template_name = "productos/index.html"
    model = Producto
