from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Song
        fields = '__all__'


class VerifySongSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    code = serializers.CharField(max_length=4)


class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Artist
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Favorite
        fields = '__all__'


class ListFavoriteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Favorite
        fields = ('id', 'user',)


class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Playlist
        fields = '__all__'


class ListLibrarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.MyLibrary
        fields = ('id', 'user')


class LibrarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.MyLibrary
        fields = '__all__'
