from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader


async def home(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("core/home.html")
    return HttpResponse(template.render({}, request))
