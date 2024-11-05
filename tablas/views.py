from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Proveedores
from .serializers import ProveedoresSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()  # Define el conjunto de datos para todos los proveedores
    serializer_class = ProveedoresSerializer  # Asocia el serializador para el modelo Proveedores

    # Sobreescribimos el método create para personalizar la respuesta
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'Proveedor creado exitosamente', 'proveedor': serializer.data}, status=status.HTTP_201_CREATED)

    # Sobreescribimos el método update para personalizar la respuesta al actualizar un proveedor
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Soporta actualizaciones parciales si partial es True
        instance = self.get_object()  # Obtiene la instancia del proveedor
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'Proveedor actualizado exitosamente', 'proveedor': serializer.data})

    # Sobreescribimos el método destroy para personalizar la respuesta al eliminar un proveedor
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'Proveedor eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
