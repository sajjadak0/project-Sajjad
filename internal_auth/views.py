from django.contrib.auth import aauthenticate, alogin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from core.utils import Methods, method_mapper
from internal_auth.form import LoginForm


async def login_view(request: HttpRequest) -> HttpResponse:
    def _send_response(form: LoginForm) -> HttpResponse:
        template = loader.get_template("auth/login.html")

        return HttpResponse(template.render(
                {"login_form": form},
                request,
            )
        )

    async def get() -> HttpResponse:
        form = LoginForm()
        return _send_response(form)

    async def post() -> HttpResponse:
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            return _send_response(form)

        user = await aauthenticate(
            request=request,
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )

        if not user:
            form.add_error(None, "Wrong credentials.")
            return _send_response(form)

        await alogin(request, user)

        return HttpResponseRedirect(reverse("core:home"))

    return await method_mapper(
        request,
        {
            Methods.GET: get,
            Methods.POST: post,
        },
    )