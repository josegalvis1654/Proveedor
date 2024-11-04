from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proveedores
from .serializers import ProveedoresSerializer

@api_view(['GET', 'POST'])
def proveedores_list(request):
    if request.method == 'GET':
        proveedores = Proveedores.objects.all()
        serializer = ProveedoresSerializer(proveedores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProveedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proveedor_detail(request, pk):
    try:
        proveedor = Proveedores.objects.get(pk=pk)
    except Proveedores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProveedoresSerializer(proveedor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProveedoresSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
