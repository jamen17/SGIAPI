

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

from empresa.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'