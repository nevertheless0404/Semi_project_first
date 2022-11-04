# Generated by Django 3.2.13 on 2022-11-04 05:40

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=30)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('Opening_hours', models.TextField()),
                ('menu', models.TextField()),
                ('price_avg', models.TextField()),
                ('parking', models.CharField(max_length=50)),
                ('day_off', models.CharField(max_length=40)),
                ('restaurant_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('category', models.CharField(choices=[('한식', '한식'), ('양식', '양식'), ('중식', '중식'), ('일식', '일식'), ('기타', '기타')], max_length=50)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('like_users', models.ManyToManyField(related_name='like_restaurant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
