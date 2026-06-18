from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader


async def SepehrView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("core/index.html")
    return HttpResponse(template.render({}, request))
