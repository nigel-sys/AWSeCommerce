from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from .models import Cart, CartItems
from products.models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@login_required
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


class CartView(LoginRequiredMixin, ListView):
    model = CartItems
    template_name = 'userProfile/cart_list.html'

    def get_queryset(self):
        return CartItems.objects.filter(user=self.request.user)


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


@login_required
def checkout(request):
    return render(request, 'userProfile/checkout.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'userProfile/register.html'
