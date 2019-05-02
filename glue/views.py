from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, World!")


def link(request, link_id):
    return HttpResponse(f"You are looking for the link with ID: {link_id}")
