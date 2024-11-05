from django.urls import path
from .views import Prov

urlpatterns = [
    path('proveedores/', Prov.crear, name='crear_proveedor'),
    path('proveedores/<int:id>/', Prov.eliminar, name='eliminar_proveedor'),
]
