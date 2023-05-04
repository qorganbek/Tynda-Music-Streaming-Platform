from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from . import models, serializer, services, permissions, filters


class SongModelViewSet(ModelViewSet):
    queryset = models.Song.objects.select_related('category')
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter
    permission_classes = (permissions.SongPermission, )


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.prefetch_related('song')
    serializer_class = serializer.ArtistSerializer
    filterset_class = filters.ArtistFilter
    permission_classes = (permissions.PlayListPermission,)


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('song')
    serializer_class = serializer.CategorySerializer
    filterset_class = filters.CategoryFilter
    permission_classes = (permissions.IsAdminOrReadOnly,)


class FavoriteModelViewSet(ModelViewSet):
    queryset = models.Favorite.objects.all()
    filterset_class = filters.FavoriteFilter
    permission_classes = (permissions.IsOwner,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializer.ListFavoriteSerializer
        return serializer.FavoriteSerializer


class LibraryModelViewSet(ModelViewSet):
    queryset = models.MyLibrary.objects.all()
    permission_classes = (permissions.IsOwner,)

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return serializer.ListLibrarySerializer
        return serializer.LibrarySerializer


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    filterset_class = filters.PlaylistFilter
    permission_classes = (permissions.PlayListPermission,)


@api_view(['POST'])
@swagger_auto_schema(request_body=serializer.SongSerializer)
def CreateSong(request, *args, **kwargs):
    service: services.SongServiceInterface = services.SongServiceV1()

    ser = serializer.SongSerializer(data=request.data)
    ser.is_valid(raise_exception=True)

    if ser.validated_data['artist'].user != request.user:
        print(ser.validated_data['artist'].user)
        return Response({'message': 'artist user not equal your user!'}, status=404)

    data = service.create_song(data=ser.validated_data)

    return Response(data, status=201)


@api_view(['POST'])
@swagger_auto_schema(request_body=serializer.VerifySongSerializer)
def VerifySong(request, *args, **kwargs):
    service: services.SongServiceInterface = services.SongServiceV1()

    ser = serializer.VerifySongSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    service.verify_song(data=ser.validated_data)
    return Response(ser.validated_data, status=201)


class SongViewSet(ViewSet):
    service: services.SongServiceInterface = services.SongServiceV1()
    permission_classes = (permissions.SongPermission,)

    @swagger_auto_schema(request_body=serializer.SongSerializer)
    def create_song(self, request, *args, **kwargs):
        ser = serializer.SongSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        if ser.validated_data['artist'].user != request.user:
            print(ser.validated_data['artist'].user)
            return Response({'message': 'artist user not equal your user!'}, status=404)

        data = self.service.create_song(data=ser.validated_data)

        return Response(data, status=201)

    @swagger_auto_schema(request_body=serializer.VerifySongSerializer)
    def verify_song(self, request, *args, **kwargs):
        ser = serializer.VerifySongSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        self.service.verify_song(data=ser.validated_data)
        return Response(ser.validated_data, status=201)
