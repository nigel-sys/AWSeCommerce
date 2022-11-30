from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.


class ProductsView(ListView):
    model = Product
    template_name = "products/product_list.html"
    paginate_by = 5


class ProductDetail(DetailView):
    model = Product
