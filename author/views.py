from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import Author
from rest_framework.response import Response

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AuthorListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.AuthorCreateUpdateSerializer
        elif self.action in ('destroy', 'retrieve'):
            return serializers.AuthorDetailSerializer

