from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Artist
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Category
        fields = '__all__'
