"""EzoPlantsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing import views as landing_views
from products import views as product_views
from orders import views as order_views
from django.conf import settings
from django.urls import include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing_views.landing),
    path('', landing_views.home),
    path(r'^product/(?P<product_id>\w+)/$', product_views.product, name='product'),
    path(r'^basket_adding/$', order_views.basket_adding, name='basket_adding'),
    path(r'^checkout/$', order_views.checkout, name='checkout'),
    path(r'^admin_orders/$', order_views.admin_orders, name='admin_orders'),

    path('all_products/', landing_views.all_products),
    path('contacts/', landing_views.contacts),


    path('summernote/', include('django_summernote.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)