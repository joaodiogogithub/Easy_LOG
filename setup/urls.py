"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main.views import ClientListView, ClientUpdateView, ClientDeleteView, ClientCreateView, StockListView, StockUpdateView, StockCreateView, StockDeleteView, home, ProductListView, ProductUpdateView, ProductCreateView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('stock/', StockListView.as_view(), name='stock_list'),
    path('stock/update/<int:pk>', StockUpdateView.as_view(), name='stock_update'),
    path('stock/create/', StockCreateView.as_view(), name='stock_create'),
    path('stock/delete/<int:pk>', StockDeleteView.as_view(), name='stock_delete'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
