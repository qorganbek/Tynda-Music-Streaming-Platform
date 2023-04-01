from django_filters import rest_framework as f
from . import models


class SongFilter(f.FilterSet):
    title = f.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = models.Song
        fields = ['title', 'id']


class CategoryFilter(f.FilterSet):
    name = f.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Category
        fields = ['name', 'id']


class ArtistFilter(f.FilterSet):
    username = f.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = models.Artist
        fields = ['username', 'id',]
