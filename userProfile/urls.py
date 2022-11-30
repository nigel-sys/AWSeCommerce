from django.urls import path
from .views import add_to_cart, CartView, remove_from_cart, update_cart

app_name = "userProfile"

urlpatterns = [
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>',
         remove_from_cart, name='remove_from_cart'),
    path("update-cart", update_cart, name="update_cart"),
    path('cart/', CartView.as_view(), name='cart')
]
