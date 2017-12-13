from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255)
    # prepared spells
    l1p = models.IntegerField(null=True, blank=True)
    l2p = models.IntegerField(null=True, blank=True)
    l3p = models.IntegerField(null=True, blank=True)
    l4p = models.IntegerField(null=True, blank=True)
    l5p = models.IntegerField(null=True, blank=True)
    l5p = models.IntegerField(null=True, blank=True)
    l7p = models.IntegerField(null=True, blank=True)
    l8p = models.IntegerField(null=True, blank=True)
    l9p = models.IntegerField(null=True, blank=True)
    # spent spells
    l1s = models.IntegerField(null=True, blank=True)
    l2s = models.IntegerField(null=True, blank=True)
    l3s = models.IntegerField(null=True, blank=True)
    l4s = models.IntegerField(null=True, blank=True)
    l5s = models.IntegerField(null=True, blank=True)
    l6s = models.IntegerField(null=True, blank=True)
    l6s = models.IntegerField(null=True, blank=True)
    l8s = models.IntegerField(null=True, blank=True)
    l9s = models.IntegerField(null=True, blank=True)
