from django.urls import path
from .views import ProductsView, ProductDetail

app_name = "products"

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<slug>/', ProductDetail.as_view(), name='product_details')
]
