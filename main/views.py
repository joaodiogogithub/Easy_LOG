from django.shortcuts import render
from .models import Estoque, Cliente, Produto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'main/home.html')

# Cliente=============================================

class ClienteListView(ListView):
    model = Cliente

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('cliente_list')
    template_name = 'main/register.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('cliente_list')
    template_name = 'main/register.html'

class ClienteDeleteView(DeleteView):
    model = Cliente
    fields = ['nome']
    success_url = reverse_lazy('cliente_list')

# Estoque=============================================

class EstoqueListView(ListView):
    model = Estoque

class EstoqueUpdateView(UpdateView):
    model = Estoque
    fields = ['materia_prima', 'quantidade']
    success_url = reverse_lazy('estoque_list')
    template_name = 'main/register.html'

class EstoqueCreateView(CreateView):
    model = Estoque
    fields = ['materia_prima', 'quantidade']
    success_url = reverse_lazy('estoque_list')
    template_name = 'main/register.html'

class EstoqueDeleteView(DeleteView):
    model = Estoque
    fields = ['materia_prima']
    success_url = reverse_lazy('estoque_list')


# Produto=============================================

class ProdutoListView(ListView):
    model = Produto

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'quantidade']
    success_url = reverse_lazy('produto_list')
    template_name = 'main/register.html'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'quantidade']
    success_url = reverse_lazy('produto_list')
    template_name = 'main/register.html'

class ProdutoDeleteView(DeleteView):
    model = Produto
    fields = ['nome']
    success_url = reverse_lazy('produto_list')
