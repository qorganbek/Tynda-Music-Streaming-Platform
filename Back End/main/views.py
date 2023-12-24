from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializer, permissions, filters, repos
from rest_framework.settings import api_settings
from . import choices as status_choices


class SongModelViewSet(ModelViewSet):
    repo: repos.SongReposInterface = repos.SongReposV1()
    queryset = models.Song.objects.filter(status=status_choices.StatuChoices.Accepted)
    serializer_class = serializer.SongSerializer
    filterset_class = filters.SongFilter
    permission_classes = (permissions.SongPermission,)

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        if request.user != ser.validated_data['artist'].user:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Your user not equal to artist user"})
        self.perform_create(ser)
        headers = self.get_success_headers(ser.data)
        return Response(ser.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, ser):
        ser.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    # def create(self, request, *args, **kwargs):
    #     ser = serializer.SongSerializer(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     if request.user != ser.validated_data['artist'].user:
    #         raise ValueError("User not equal artist user")
    #     self.repo.create_song(data=ser.validated_data)
    #     return Response(ser.validated_data, status=status.HTTP_201_CREATED)


class ArtistModelViewSet(ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializer.ArtistSerializer
    filterset_class = filters.ArtistFilter
    permission_classes = (permissions.PlayListPermission,)


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
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
        # if self.action == 'retrieve':
        #     return serializer.RetrieveLibrarySerializer
        return serializer.LibrarySerializer


class PlaylistModelViewSet(ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializer.PlaylistSerializer
    permission_classes = (permissions.PlayListPermission,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializer.RetrievePlaylistSerializer
        return serializer.PlaylistSerializer

# @api_view(['POST'])
# @swagger_auto_schema(request_body=serializer.SongSerializer)
# def CreateSong(request, *args, **kwargs):
#     service: services.SongServiceInterface = services.SongServiceV1()
#
#     ser = serializer.SongSerializer(data=request.data)
#     ser.is_valid(raise_exception=True)
#
#     if ser.validated_data['artist'].user != request.user:
#         print(ser.validated_data['artist'].user)
#         return Response({'message': 'artist user not equal your user!'}, status=404)
#
#     data = service.create_song(data=ser.validated_data)
#
#     return Response(data, status=201)
#
#
# @api_view(['POST'])
# @swagger_auto_schema(request_body=serializer.VerifySongSerializer)
# def VerifySong(request, *args, **kwargs):
#     service: services.SongServiceInterface = services.SongServiceV1()
#
#     ser = serializer.VerifySongSerializer(data=request.data)
#     ser.is_valid(raise_exception=True)
#     service.verify_song(data=ser.validated_data)
#     return Response(ser.validated_data, status=201)


# class SongViewSet(ViewSet):
#     service: services.SongServiceInterface = services.SongServiceV1()
#     permission_classes = (permissions.SongPermission,)
#
#     @swagger_auto_schema(request_body=serializer.SongSerializer)
#     def create_song(self, request, *args, **kwargs):
#         ser = serializer.SongSerializer(data=request.data)
#         ser.is_valid(raise_exception=True)
#
#         if ser.validated_data['artist'].user != request.user:
#             print(ser.validated_data['artist'].user)
#             return Response({'message': 'artist user not equal your user!'}, status=404)
#
#         data = self.service.create_song(data=ser.validated_data)
#
#         return Response(data, status=201)
#
#     @swagger_auto_schema(request_body=serializer.VerifySongSerializer)
#     def verify_song(self, request, *args, **kwargs):
#         ser = serializer.VerifySongSerializer(data=request.data)
#         ser.is_valid(raise_exception=True)
#         self.service.verify_song(data=ser.validated_data)
#         return Response(ser.validated_data, status=201)


#  channel with websocket
#  account reset password and another fixtures
#  presentation
#  video +-
