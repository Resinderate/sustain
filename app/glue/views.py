from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, World!")


def hello_moon(request):
    return HttpResponse("Hello, Moon!")
