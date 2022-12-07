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


class FilteredView(ListView):
    model = Product
    template_name = "products/product_filtered_list.html"
    paginate_by = 5

    def get_queryset(self):
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        return products
