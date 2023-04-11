from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'password')
