from django.db import models
from . import Handler


class Subscriptions(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Threshold(models.Model):
    LEVELS = (
        (0, 'ok'),
        (1, 'warning'),
        (2, 'critical'),
        (3, 'unknown'),
    )

    name = models.IntegerField(choices=LEVELS)

    def __unicode__(self):
        return self.name


class ThresholdLevel(models.Model):
    threshold = models.ForeignKey(Threshold)
    interval = models.IntegerField(default=60)


class KeepAlive(models.Model):
    threshold = models.ManyToManyField(ThresholdLevel)
    handlers = models.ManyToManyField(Handler)
    refresh = models.IntegerField(default=1800)


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    subscriptions = models.ManyToManyField(Subscriptions)
    handlers = models.ManyToManyField(Handler)
    keepAlive = models.ForeignKey(KeepAlive)

