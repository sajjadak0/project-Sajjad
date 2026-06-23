from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from core.services.email_services import validate_token


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
