from dataclasses import dataclass

from core.models import ResetPassword


@dataclass
class ResetPasswordResult:
    error: str | None
    reset_password_model: ResetPassword | None
