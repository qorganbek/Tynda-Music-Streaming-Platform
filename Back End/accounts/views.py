from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import serializers, services


class UserViewSet(ViewSet):
    user_service: services.UserServiceInterface = services.UserServicesV1()

    @swagger_auto_schema(request_body=serializers.CreateUserSerializer)
    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = self.user_service.create_user(data=serializer.validated_data)

        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=serializers.VerifyUserSerializer)
    def verify_user(self, request, *args, **kwargs):
        serializer = serializers.VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.user_service.verify_user(data=serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
