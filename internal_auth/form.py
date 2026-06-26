from django import forms

from core.form import BaseForm


class LoginForm(BaseForm):
    email = forms.EmailField(
        label="Email:",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
            },
        ),
    )

    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
            },
        ),
    )
