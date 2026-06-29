from typing import Any
from django import forms


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(min_length=8)
    confirm_password = forms.CharField(min_length=8)

    def clean(self) -> dict[str, Any]:
        cleaned_data: dict[str, Any] = super().clean() or {}

        password1 = cleaned_data.get("new_password")
        password2 = cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords do not match")

        return cleaned_data
