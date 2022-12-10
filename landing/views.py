from django.shortcuts import render
import datetime
from products.models import *

def landing(request):
    name = "vladislavister"
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_kratom = products_images.filter(product__category_id=1)
    products_images_chinese_tea = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals())

def all_products(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_kratom = products_images.filter(product__category_id=1)
    products_images_chinese_tea = products_images.filter(product__category_id=2)
    return render(request, 'landing/all_products.html', locals())
def contacts(request):
    return render(request, 'landing/contacts.html', locals())
