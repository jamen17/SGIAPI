from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from empresa.models import *
from empresa.serializers import *

'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   @action(methods=['post'])
    def set_comment(self, request, pk=None):
        my_post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=my_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    #filterset_fields = ['category', 'in_stock']
class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filterset_fields = ['empresa']

    @action(methods=['post'],detail=True)
    def set_sucursal(self, request, pk=None):
        empresa = self.get_object()
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(empresa=empresa)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer
    filterset_fields = ['sucursal']

    @action(methods=['post'],detail=True)
    def set_dependencia(self, request, pk=None):
        sucursal = self.get_object()
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sucursal=sucursal)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filterset_fields = ['dependencia']

    @action(methods=['post'],detail=True)
    def set_cargo(self, request, pk=None):
        dependencia = self.get_object()
        serializer = DependenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(dependencia=dependencia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Competencia.objects.all()
    serializer_class = PerfilSerializer
    filterset_fields = ['cargo']

    @action(methods=['post'],detail=True)
    def set_perfil(self, request, pk=None):
        cargo = self.get_object()
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cargo=cargo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
