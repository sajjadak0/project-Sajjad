from django.contrib.auth import aauthenticate, alogin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from internal_auth.form import LoginForm


async def login_view(request: HttpRequest) -> HttpResponse:
    def _send_response(form: LoginForm) -> HttpResponse:
        template = loader.get_template("auth/login.html")

        return HttpResponse(
            template.render(
                {
                    "login_form": form,
                },
                request,
            )
        )

    if request.method == "GET":
        form = LoginForm()
        return _send_response(form)

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            return _send_response(form)

        user = await aauthenticate(
            request=request,
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )

        if not user:
            form.add_error(None, "ایمیل یا رمز عبور اشتباه است.")
            return _send_response(form)

        await alogin(request, user)

        return HttpResponseRedirect(reverse("core:home"))

    return HttpResponse(status=405)
