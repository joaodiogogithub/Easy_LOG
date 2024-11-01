from django.shortcuts import render
from .models import Stock, Client, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import smtplib

def home(request):
    return render(request, 'main/home.html')
# Cliente=============================================

class ClientListView(ListView):
    model = Client

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'number', 'address']
    success_url = reverse_lazy('client_list')
    template_name = 'main/register.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'number', 'address']
    success_url = reverse_lazy('client_list')
    template_name = 'main/register.html'

class ClientDeleteView(DeleteView):
    model = Client
    fields = ['name']
    success_url = reverse_lazy('client_list')

class ClientSendEmailView(UpdateView):
    model = Client
    fields = ['name', 'email']
    success_url = reverse_lazy('client_list')
    template_name = 'main/send_email.html'


# Estoque=============================================

class StockListView(ListView):
    model = Stock

class StockUpdateView(UpdateView):
    model = Stock
    fields = ['materia', 'quanty']
    success_url = reverse_lazy('stock_list')
    template_name = 'main/register.html'

class StockCreateView(CreateView):
    model = Stock
    fields = ['materia', 'quanty']
    success_url = reverse_lazy('stock_list')
    template_name = 'main/register.html'

class StockDeleteView(DeleteView):
    model = Stock
    fields = ['materia']
    success_url = reverse_lazy('stock_list')


# Produto=============================================

class ProductListView(ListView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'quanty']
    success_url = reverse_lazy('product_list')
    template_name = 'main/register.html'

class ProductCreateView(CreateView):
    model = Product
    fields =  ['name', 'description', 'price', 'quanty']
    success_url = reverse_lazy('product_list')
    template_name = 'main/register.html'

class ProductDeleteView(DeleteView):
    model = Product
    fields = ['name']
    success_url = reverse_lazy('product_list')
