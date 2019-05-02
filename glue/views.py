from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Link


def hello_world(request):
    return HttpResponse("Hello, World!")


def link(request, slug):
    link = get_object_or_404(Link, slug=slug)

    copy = link.copies.first()

    return redirect(copy.url)
