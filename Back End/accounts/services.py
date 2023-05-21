import random
import uuid
from typing import Protocol, OrderedDict
from django.core.cache import cache
from templated_email import send_templated_mail
from src import settings
from . import models, repos


class UserServiceInterface(Protocol):

    def create_user(self, data: OrderedDict) -> dict: ...

    def verify_user(self, data: OrderedDict) -> None: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> dict:
        session_id = self._verify_email(data=data)

        return {
            "session_id": session_id
        }

    def verify_user(self, data: OrderedDict) -> None:
        user_data = cache.get(data['session_id'])

        if not user_data:
            raise ValueError('Session ID not correct')

        code_new = user_data.pop('code')

        if data['code'] != code_new:
            raise ValueError('Code not correct')

        user = self.user_repos.create_user(data=user_data)
        self._send_letter_to_email(user)

    def _verify_email(self, data: OrderedDict) -> str:
        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {'code': code, **data}, timeout=300)
        self._send_letter_to_email_verify(data['email'], code)
        return session_id

    @staticmethod
    def _send_letter_to_email(user: models.CustomUser) -> None:
        send_templated_mail(
            template_name='welcome',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            context={
                'id': user.id,
                'email': user.email,
            },
        )

    @staticmethod
    def _send_letter_to_email_verify(email: str, code: str) -> None:
        send_templated_mail(
            template_name='verify',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            context={
                'code': code,
            },
        )

    @staticmethod
    def _generate_code(length: int = 4) -> str:
        numbers = [str(x) for x in range(10)]
        return ''.join(random.choices(numbers, k=length))

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())
