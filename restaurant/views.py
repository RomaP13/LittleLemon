from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def sayHello(request: HttpRequest):
    return HttpResponse("Hello")


def index(request: HttpRequest):
    return render(request, "index.html", {})
