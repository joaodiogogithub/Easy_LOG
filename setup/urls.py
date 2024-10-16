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
from main.views import ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteCreateView, EstoqueListView, EstoqueUpdateView, EstoqueCreateView, EstoqueDeleteView, home, ProdutoListView, ProdutoUpdateView, ProdutoCreateView, ProdutoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),

    path('cliente/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<int:pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>', ClienteDeleteView.as_view(), name='cliente_delete'),

    path('estoque/', EstoqueListView.as_view(), name='estoque_list'),
    path('estoque/update/<int:pk>', EstoqueUpdateView.as_view(), name='estoque_update'),
    path('estoque/create/', EstoqueCreateView.as_view(), name='estoque_create'),
    path('estoque/delete/<int:pk>', EstoqueDeleteView.as_view(), name='estoque_delete'),

    path('produto/', ProdutoListView.as_view(), name='produto_list'),
    path('produto/update/<int:pk>', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/create/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/delete/<int:pk>', ProdutoDeleteView.as_view(), name='produto_delete'),
]
