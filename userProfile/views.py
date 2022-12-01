from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Cart, CartItems
from products.models import Product
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse, reverse_lazy
import json

# Create your views here.


def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    user = request.user
    cart = Cart.objects.filter(user=user, is_paid=False)
    cart_item, created = CartItems.objects.get_or_create(
        product=product, user=user, is_paid=False)
    if cart.exists():
        order = cart[0]
        if order.items.filter(product__slug=product.slug).exists():
            cart_item.quantity += 1
            cart_item.save()
        else:
            order.items.add(cart_item)
    else:
        order = Cart.objects.create(user=user, is_paid=False)
        order.items.add(cart_item)

    return redirect(reverse('userProfile:cart'))


class CartView(ListView):
    model = CartItems
    template_name = 'userProfile/cart_list.html'


def remove_from_cart(request, slug):
    product = Product.objects.get(slug=slug)
    user = request.user
    cart = Cart.objects.filter(user=user, is_paid=False)

    if cart.exists():
        order = cart[0]
        if order.items.filter(product__slug=product.slug).exists():
            cart_item = CartItems.objects.filter(
                product=product, user=user, is_paid=False)[0]
            order.items.remove(cart_item)
            cart_item.delete()
        else:
            # cart item not present in cart message
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        # cart empty / user doesn't have an order message
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_singleitem_from_cart(request, slug):
    product = Product.objects.get(slug=slug)
    user = request.user
    cart = Cart.objects.filter(user=user, is_paid=False)

    if cart.exists():
        order = cart[0]
        if order.items.filter(product__slug=product.slug).exists():
            cart_item = CartItems.objects.filter(
                product=product, user=user, is_paid=False)[0]
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
        else:
            # cart item not present in cart message
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        # cart empty / user doesn't have an order message
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
