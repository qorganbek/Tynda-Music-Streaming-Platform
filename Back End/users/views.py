from rest_framework import viewsets
from users import models, serializers


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
