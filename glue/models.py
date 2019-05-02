from django.db import models


class Link(models.Model):
    master_url = models.URLField()
    slug = models.SlugField()


class LinkPointer(models.Model):
    parent = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="copies")
    url = models.URLField()
