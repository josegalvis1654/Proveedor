from rest_framework import viewsets
from rest_framework.response import Response
from .models import Proveedores
from .serializers import ProveedoresSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class Prov:
    def crear(self, request):
        if request.method == 'POST':
            proveedor = Proveedores(
            nit=request.POST['nit'],
            razon_social=request.POST['razon_social'],
            representante_legal=request.POST['representante_legal'],
            direccion=request.POST['direcion'], 
            vehiculo_asociado=request.POST['vehiculo_asociado']
            )
            proveedor.save()
            return Response({'error': 'Faltan datos necesarios'}, status=400)
    def eliminar(self, request, id):
        proveedor = Proveedores.objects.get(id=id)
        proveedor.delete