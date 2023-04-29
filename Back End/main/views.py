from django.contrib.auth import get_user_model
from rest_framework.response import Response
from . import filters
from rest_framework.viewsets import ModelViewSet, ViewSet
from . import models, serializer
from . import permissions
from rest_framework import permissions as rest_permissions, status


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter


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
    permission_classes = (permissions.IsOwner, )


class LibraryModelViewSet(ModelViewSet):
    queryset = models.MyLibrary.objects.all()
    serializer_class = serializer.LibrarySerializer
    permission_classes = (permissions.IsOwner, )


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    filterset_class = filters.PlaylistFilter
    permission_classes = (rest_permissions.IsAdminUser,)


class CreateUserViewSet(ViewSet):

    def create_user(self, request, **kwargs):
        ser = serializer.CreateUserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        model = get_user_model()
        model.objects.create(**ser.validated_data)
        return Response({'message': 'created'}, status=status.HTTP_201_CREATED)

#
# def MainPage(request):
#     return render(request, 'index.html')
