from django.urls import path
from .views import add_to_cart, CartView, remove_from_cart, remove_singleitem_from_cart

app_name = "userProfile"

urlpatterns = [
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>',
         remove_from_cart, name='remove_from_cart'),
    path('remove-singleitem-from-cart/<slug>',
         remove_singleitem_from_cart, name='remove_singleitem'),
    path('cart/', CartView.as_view(), name='cart')
]
