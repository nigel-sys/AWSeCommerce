from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile')

    def cart_count(self):
        return CartItems.objects.filter(cart__is_paid=False, cart__user=self.user).count()


class CartItems(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(CartItems)
    is_paid = models.BooleanField(default=False)
