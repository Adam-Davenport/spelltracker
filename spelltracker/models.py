from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255)
    # prepared spells
    l1p = models.IntegerField(default=0)
    l2p = models.IntegerField(default=0)
    l3p = models.IntegerField(default=0)
    l4p = models.IntegerField(default=0)
    l5p = models.IntegerField(default=0)
    l5p = models.IntegerField(default=0)
    l7p = models.IntegerField(default=0)
    l8p = models.IntegerField(default=0)
    l9p = models.IntegerField(default=0)
    # spent spells
    l1s = models.IntegerField(default=0)
    l2s = models.IntegerField(default=0)
    l3s = models.IntegerField(default=0)
    l4s = models.IntegerField(default=0)
    l5s = models.IntegerField(default=0)
    l6s = models.IntegerField(default=0)
    l6s = models.IntegerField(default=0)
    l8s = models.IntegerField(default=0)
    l9s = models.IntegerField(default=0)
