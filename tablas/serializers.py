from rest_framework import serializers
from .models import Proveedores

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
