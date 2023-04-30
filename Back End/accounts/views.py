from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src import settings
from . import serializers
from .models import CustomUser
from templated_email import send_templated_mail


class UserViewSet(ViewSet):

    @swagger_auto_schema(request_body=serializers.CreateUserSerializer)
    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.create_user(**serializer.validated_data)
        self._send_message_to_email(user=user)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    @staticmethod
    def _send_message_to_email(user: CustomUser) -> None:
        send_templated_mail(
            template_name='welcome',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            context={
                'email': user.email
            }
        )


