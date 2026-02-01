from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductoForm
from .models import Producto

# Create your views here.

class ProductoListView (ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"
    ordering = ["nombre"]


class ProductoCreateView (CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy("producto_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modo"] = "crear"
        return context




class ProductoUpdateView (UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy("producto_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modo"] = "editar"
        return context


class DeleteProductoView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("producto_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().delete(request, *args, **kwargs)