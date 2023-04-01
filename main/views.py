from rest_framework.viewsets import ModelViewSet
from . import models, serializer


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializer.SongSerializer


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializer.ArtistSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
