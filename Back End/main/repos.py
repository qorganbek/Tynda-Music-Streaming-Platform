from typing import Protocol, OrderedDict
from . import models


class SongReposInterface(Protocol):
    def create_song(self, data: OrderedDict) -> models.Song: ...


class SongReposV1:

    def create_song(self, data: OrderedDict) -> models.Song:
        return models.Song.objects.create(**data)
