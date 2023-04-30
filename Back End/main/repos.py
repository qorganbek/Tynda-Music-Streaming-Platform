from typing import Protocol, OrderedDict
from . import models


class SongReposInterface(Protocol):
    def create_song(self, data: OrderedDict) -> models.Song: ...


class SongReposV1:
    model: models.Song = models.Song

    def create_song(self, data: OrderedDict) -> models.Song:
        return self.model.objects.create(**data)
