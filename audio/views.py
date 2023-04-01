from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer


class AudioViewSet(ModelViewSet):
    queryset = models.Audio.objects.all()
    serializer_class = serializer.AudioSerializer
