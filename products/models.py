from django.db import models
import uuid
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    CATEGORIES = (
        ('computers', 'COMPUTERS'),
        ('mobile', 'MOBILES'),
        ('tvs', 'TVs'),
        ('cameras', 'CAMERAS'),
        ('speakers', 'SPEAKERS')
    )
    category_name = models.CharField(
        max_length=10, choices=CATEGORIES, default='computers')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self):
        self.slug = slugify(self.category_name)
        super(Category, self).save()

    def __str__(self):
        return f"Category: {self.category_name}"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()
    product_image = models.ImageField(
        upload_to='products', default="/media/images/no_product_image.png")
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self):
        self.slug = slugify(self.product_name)
        super(Product, self).save()

    def __str__(self):
        return f"Product: {self.product_name} {self.price} {self.product_description}"
