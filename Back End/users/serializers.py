from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.CustomUser
        fields = '__all__'
