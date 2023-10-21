from rest_framework import serializers
from films.models import Film 


class FilmSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Film
        fields = ('id', 'name', 'director', 'description', 'image')