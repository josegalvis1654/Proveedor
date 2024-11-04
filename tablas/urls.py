from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('proveedores/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
]
