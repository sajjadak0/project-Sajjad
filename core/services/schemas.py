from dataclasses import dataclass

from core.models import ResetPasswordModel


@dataclass
class ResetPasswordResult:
    error: str | None
    reset_password_model: ResetPasswordModel | None
