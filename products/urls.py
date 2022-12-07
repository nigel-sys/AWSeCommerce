from django.urls import path
from .views import ProductsView, ProductDetail, FilteredView

app_name = "products"

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<slug>/', ProductDetail.as_view(), name='product_details'),
    path("products/<slug>/", FilteredView.as_view(), name="category")
]
