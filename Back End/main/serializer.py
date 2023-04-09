from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Song
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    song = SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Artist
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    song = SongSerializer(read_only=True, many=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Favorite
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Playlist
        fields = '__all__'
