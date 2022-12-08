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


def search_products(request):
    query_dict = request.GET
    query = query_dict.get("q")  # <input type="search" name="q"/>
    product = None
    if query is not None:
        product = Product.objects.get(product_name__contains=query)
    context = {
        'product': product
    }
    return render(request, 'products/search.html', context=context)
