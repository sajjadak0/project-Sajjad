import secrets
from datetime import timedelta, datetime
from django.utils import timezone

from core.models import ResetPassword, UserModel


def _token_generator() -> tuple[str, datetime]:
    token = secrets.token_urlsafe(32)
    expires_at = timezone.now() + timedelta(minutes=15)
    return token, expires_at


def create_magic_link(user: UserModel) -> str:
    token, expires_at = _token_generator()
    ResetPassword.objects.create(user=user, token=token, expires_at=expires_at)
    return token
