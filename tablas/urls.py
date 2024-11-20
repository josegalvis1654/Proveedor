from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet,ObtenerProveedorView

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('proveedores/maxlotes/<int:proveedor_id>/', ObtenerProveedorView.as_view(), name='proveedoresmaxlotes')
]
