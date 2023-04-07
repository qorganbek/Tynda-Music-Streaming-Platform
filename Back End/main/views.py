from django.shortcuts import render
from . import filters
from rest_framework.viewsets import ModelViewSet
from . import models, serializer


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter


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


def MainPage(request):
    return render(request, 'index.html')
