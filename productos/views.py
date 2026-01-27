from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

from .forms import ProductoForm
from .models import Producto

# Create your views here.
def producto_list(request):
    productos = Producto.objects.all().order_by('nombre')
    return render (request, "productos/producto_list.html",{"productos":productos})

def producto_create(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto creado correctamente.")
        return redirect("producto_list")
    return render (request, "productos/producto_form.html", {"form": form, "modo":"crear"})

def producto_update(request,pk):
    producto = get_object_or_404(Producto,pk = pk)
    form = ProductoForm(request.POST or None,instance=producto)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado correctamente.")
        return redirect("producto_list")
    return render (request, "productos/producto_form.html", {"form": form, "modo":"editar","producto":producto})

def producto_delete(request,pk):
    producto =  get_object_or_404(Producto,pk = pk)
    if request.method == "POST":
        producto.delete()
        messages.success(request,"Producto eliminado correctamente.")
        return redirect("producto_list")
    return render (request, "productos/producto_confirm_delete.html", {"producto":producto})
