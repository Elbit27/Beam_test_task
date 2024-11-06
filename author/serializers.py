from django.template.context_processors import request
from rest_framework import serializers
from .models import Author

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        return author

