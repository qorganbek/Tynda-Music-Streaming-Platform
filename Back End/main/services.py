import random
import uuid
from typing import Protocol, OrderedDict
from django.core.cache import cache
from templated_email import send_templated_mail
from src import settings
from . import models, repos
from accounts.models import CustomUser


class SongServiceInterface(Protocol):
    def create_song(self, data: OrderedDict) -> dict: ...

    def verify_song(self, data: OrderedDict) -> models.Song | None: ...


class SongServiceV1:
    repo: repos.SongReposInterface = repos.SongReposV1()

    def create_song(self, data: OrderedDict) -> dict:
        session_id = self._verify_email(data=data)

        return {
            'session_id': session_id
        }

    def verify_song(self, data: OrderedDict) -> None:
        song_data = cache.get(data['session_id'])

        if not song_data:
            return

        code_new = song_data.pop('code')

        if data['code'] != code_new:
            return

        self.repo.create_song(data=song_data)

    def _verify_email(self, data: OrderedDict) -> str:
        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {'code': code, **data}, timeout=300)
        self._send_code_to_email(data['artist'].user.email, code)
        return session_id

    @staticmethod
    def _send_code_to_email(email: str, code: str) -> None:
        send_templated_mail(
            template_name='song',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            context={
                'email': email,
                'code': code
            },
        )

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def _generate_code(length: int = 4) -> str:
        numbers = [str(x) for x in range(10)]
        return ''.join(random.choices(numbers, k=length))
