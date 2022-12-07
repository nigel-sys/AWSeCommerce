from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
# Create your views here.


class ProductsView(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product


class FilteredView(ListView):
    model = Product
    template_name = "products/product_filtered_list.html"
    paginate_by = 5

    def get_queryset(self):
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context
