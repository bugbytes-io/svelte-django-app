from rest_framework import serializers
from films.models import Film 
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class FilmSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    tags = TagListSerializerField(default=[])
    
    class Meta:
        model = Film
        fields = ('id', 'name', 'director', 'description', 'image', 'tags')