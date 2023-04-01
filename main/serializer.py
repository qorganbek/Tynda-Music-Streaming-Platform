from rest_framework import serializers
from . import models


class _CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']


class _ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = ['username']


class SongSerializer(serializers.ModelSerializer):
    artist = _ArtistSerializer(read_only=True, many=True)
    category = _CategorySerializer(read_only=True)

    class Meta:
        model = models.Song
        fields = '__all__'


class _SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['title']


class ArtistSerializer(serializers.ModelSerializer):
    songs = _SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Artist
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    songs = _SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Category
        fields = '__all__'
