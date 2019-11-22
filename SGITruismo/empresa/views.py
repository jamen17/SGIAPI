from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer

'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @detail_route(methods=['post'])
    def set_comment(self, request, pk=None):

        #get post object
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
