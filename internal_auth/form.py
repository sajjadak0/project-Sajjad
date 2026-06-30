from django import forms

from core.form import BaseForm


class LoginForm(BaseForm):
    email = forms.EmailField(
        label="ایمیل:",
        error_messages={
            "required": "وارد کردن ایمیل الزامی است.",
            "invalid": "فرمت ایمیل معتبر نیست.",
        },
        widget=forms.EmailInput(
            attrs={
                "placeholder": "ایمیل خود را وارد کنید",
                "dir": "rtl",
                "style": "text-align: right;",
            },
        ),
    )

    password = forms.CharField(
        label="رمز عبور:",
        error_messages={
            "required": "وارد کردن رمز عبور الزامی است.",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور خود را وارد کنید",
                "dir": "rtl",
                "style": "text-align: right;",
            },
        ),
    )
