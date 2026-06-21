import secrets
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta, datetime
from django.utils import timezone

from core.models import ResetPassword, UserModel


def _token_generator() -> tuple[str, datetime]:
    token = secrets.token_urlsafe(32)
    expires_at = timezone.now() + timedelta(minutes=15)
    return token, expires_at


def _send_reset_email(email: str, token: str) -> None:
    reset_link = f"http://localhost:5173/reset-password?token={token}"
    subject = "Reset your password"
    message = f"""
    Click the link below to reset your password:

    {reset_link}

    This link will expire in 15 minutes.
    """
    send_mail(
        subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False
    )


def create_magic_link(user: UserModel) -> str:
    token, expires_at = _token_generator()
    ResetPassword.objects.create(user=user, token=token, expires_at=expires_at)
    _send_reset_email(user.email, token)
    return token
