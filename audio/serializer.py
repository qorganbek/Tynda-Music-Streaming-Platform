from rest_framework import serializers
from . import models


class AudioSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Audio
        fields = '__all__'
