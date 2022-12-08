# Generated by Django 3.2.16 on 2022-12-08 20:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category_name', models.CharField(choices=[('COMPUTERS', 'computers'), ('MOBILES', 'mobiles'), ('TVs', 'tvs'), ('CAMERAS', 'cameras'), ('SPEAKERS', 'speakers')], default='COMPUTERS', max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(default='/media/images/no_product_image.png', upload_to='products')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
        ),
    ]
