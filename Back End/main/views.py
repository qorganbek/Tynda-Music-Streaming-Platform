from django.shortcuts import render
from . import filters
from rest_framework.viewsets import ModelViewSet
from . import models, serializer
from rest_framework.permissions import IsAuthenticated


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter
    # permission_classes = [IsAuthenticated]


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.prefetch_related('song')
    serializer_class = serializer.ArtistSerializer
    filterset_class = filters.ArtistFilter


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('song')
    serializer_class = serializer.CategorySerializer
    filterset_class = filters.CategoryFilter


class FavoriteModelViewSet(ModelViewSet):
    queryset = models.Favorite.objects.all()
    serializer_class = serializer.FavoriteSerializer
    filterset_class = filters.FavoriteFilter


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    filterset_class = filters.PlaylistFilter


def MainPage(request):
    return render(request, 'index.html')
