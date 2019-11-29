

'''
class PostSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserProfile.objects.all(), source='owner')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'ownerId', 'comments')
'''
from rest_framework import serializers

from empresa.models import *


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class SucursalSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empresa.objects.all(), source='empresa')
    class Meta:
        model = Sucursal
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    sucursal = SucursalSerializer(read_only=True)
    sucursal_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sucursal.objects.all(), source='sucursal')
    class Meta:
        model = Dependencia
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    dependencia = DependenciaSerializer(read_only=True)
    dependencia_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Dependencia.objects.all(), source='dependencia')
    class Meta:
        model = Cargo
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer(read_only=True)
    cargo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cargo.objects.all(), source='cargo')
    class Meta:
        model = Competencia
        fields = '__all__'