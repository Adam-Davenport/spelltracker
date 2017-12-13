from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    # prepared spells
    l1p = models.IntegerField()
    l2p = models.IntegerField()
    l3p = models.IntegerField()
    l4p = models.IntegerField()
    l5p = models.IntegerField()
    l5p = models.IntegerField()
    l7p = models.IntegerField()
    l8p = models.IntegerField()
    l9p = models.IntegerField()
    # spent spells
    l1s = models.IntegerField()
    l2s = models.IntegerField()
    l3s = models.IntegerField()
    l4s = models.IntegerField()
    l5s = models.IntegerField()
    l6s = models.IntegerField()
    l6s = models.IntegerField()
    l8s = models.IntegerField()
    l9s = models.IntegerField()
