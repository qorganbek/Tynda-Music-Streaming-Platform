from typing import Protocol, OrderedDict

from django.contrib.auth.hashers import make_password
from rest_framework.generics import get_object_or_404
from . import models


class UserReposInterface(Protocol):

    def create_user(self, data: OrderedDict) -> models.CustomUser: ...

    def get_user(self, data): ...


class UserReposV1:

    def create_user(self, data: OrderedDict) -> models.CustomUser:
        hashed_password = make_password(data.pop('password'))

        return models.CustomUser.objects.create(password=hashed_password, **data)

    def get_user(self, data):
        return get_object_or_404(models.CustomUser, **data)
