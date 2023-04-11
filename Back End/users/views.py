from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from users import models, serializers


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ViewSet):

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = models.CustomUser.objects.create(**serializer.validated_data)
        Response(data, status=status.HTTP_201_CREATED)

