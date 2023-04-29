from . import filters
from rest_framework.viewsets import ModelViewSet
from . import models, serializer
from . import permissions
from rest_framework import permissions as rest_permissions


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter
    # permission_classes = (permissions.IsAdminOrReadOnly, )


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.prefetch_related('song')
    serializer_class = serializer.ArtistSerializer
    filterset_class = filters.ArtistFilter
    # permission_classes = (permissions.IsAdminOrReadOnly,)


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('song')
    serializer_class = serializer.CategorySerializer
    filterset_class = filters.CategoryFilter
    permission_classes = (permissions.IsAdminOrReadOnly,)


class FavoriteModelViewSet(ModelViewSet):
    queryset = models.Favorite.objects.all()
    filterset_class = filters.FavoriteFilter
    permission_classes = (permissions.IsOwner, )

    def get_serializer_class(self):
        if self.action == 'list':
            return serializer.ListFavoriteSerializer
        return serializer.FavoriteSerializer


class LibraryModelViewSet(ModelViewSet):
    queryset = models.MyLibrary.objects.all()
    permission_classes = (permissions.IsOwner, )

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return serializer.ListLibrarySerializer
        return serializer.LibrarySerializer


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    filterset_class = filters.PlaylistFilter
    # permission_classes = (permissions.IsOwner, rest_permissions.IsAuthenticatedOrReadOnly, )


'''
    Permissions: Song, Playlist, Artist
    Song: Create, Verify with sending message to email
    How to post data from postman
'''
