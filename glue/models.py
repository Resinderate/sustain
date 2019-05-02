from django.db import models


class Link(models.Model):
    url = models.URLField()


class LinkPointer(models.Model):
    parent = models.ForeignKey(Link, on_delete=models.CASCADE)
