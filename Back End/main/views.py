from django.shortcuts import render
from . import filters
from rest_framework.viewsets import ModelViewSet
from . import models, serializer
from . import permissions


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter
    permission_classes = (permissions.IsAdminOrReadOnly,)


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.prefetch_related('song')
    serializer_class = serializer.ArtistSerializer
    filterset_class = filters.ArtistFilter
    permission_classes = (permissions.IsAdminOrReadOnly,)


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('song')
    serializer_class = serializer.CategorySerializer
    filterset_class = filters.CategoryFilter
    permission_classes = (permissions.IsAdminOrReadOnly,)


class FavoriteModelViewSet(ModelViewSet):
    queryset = models.Favorite.objects.all()
    serializer_class = serializer.FavoriteSerializer
    filterset_class = filters.FavoriteFilter
    permission_classes = (permissions.FavoritePermission,)


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    filterset_class = filters.PlaylistFilter


def MainPage(request):
    return render(request, 'index.html')
