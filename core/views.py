from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from core.forms import ResetPasswordForm
from core.services.email_services import set_new_password, validate_token


async def SepehrView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("core/index.html")
    return HttpResponse(template.render({}, request))


class ResetPasswordView(View):
    async def get(self, request: HttpRequest) -> HttpResponse:

        token = request.GET.get("token")
        if not token:
            return render(request, "invalid_link.html")

        result = await validate_token(token)
        if result.error:
            return HttpResponse(
                loader.get_template("core/invalid_link.html").render({}, request)
            )
        else:
            return HttpResponse(
                loader.get_template("core/reset_password_form.html").render(
                    {"result": result}, request
                )
            )

    async def post(self, request: HttpRequest) -> HttpResponse:
        token = request.GET.get("token")

        if not token:
            return HttpResponse(
                loader.get_template("core/invalid_link.html").render({}, request)
            )

        form = ResetPasswordForm(request.POST)

        valid_token = await validate_token(token)

        if valid_token.error:
            return HttpResponse(
                loader.get_template("core/invalid_link.html").render({}, request)
            )

        if form.is_valid():
            data = form.cleaned_data

            new_password: str = data["new_password"]

            await set_new_password(new_password, token)

            return HttpResponse(
                loader.get_template("core/password_reset_done.html").render({}, request)
            )

        return HttpResponse(
            loader.get_template("core/reset_password_form.html").render(
                {"form": form}, request
            )
        )
