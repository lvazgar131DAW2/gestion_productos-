from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, DeleteProductoView

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('nuevo/',ProductoCreateView.as_view(),name='producto_create'),
    path('editar/<int:pk>',ProductoUpdateView.as_view(),name='producto_update'),
    path('eliminar/<int:pk>',DeleteProductoView.as_view(),name='producto_delete'),
]