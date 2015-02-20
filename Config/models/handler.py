from django.db import models


class Handler(models.Model):
    name = models.CharField(max_length=50)
