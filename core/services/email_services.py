import secrets
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta, datetime
from django.forms import ValidationError
from django.utils import timezone

from core.models import ResetPassword, UserModel
from core.services.schemas import ResetPasswordResult


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


async def create_magic_link(user: UserModel) -> str:
    token, expires_at = _token_generator()
    await ResetPassword.objects.acreate(user=user, token=token, expires_at=expires_at)
    _send_reset_email(user.email, token)
    return token


async def validate_token(token: str) -> ResetPasswordResult:
    error: str | None = None
    reset_token: ResetPassword | None = None
    if not token:
        error = "invalid link"
    else:
        try:
            reset_token = await ResetPassword.objects.aget(token=token)
        except ResetPassword.DoesNotExist:
            error = "Token does not exist"
        if reset_token and reset_token.is_used:
            error = "Token already used"
        if reset_token and reset_token.expires_at < timezone.now():
            error = "Token expired"

    return ResetPasswordResult(error=error, reset_password_model=reset_token)
