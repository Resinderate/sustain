from django.contrib import admin

from .models import Link, LinkPointer

admin.site.register(Link)
admin.site.register(LinkPointer)
