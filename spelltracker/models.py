from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255)
    # prepared spells
    l1p = models.IntegerField(default=0)
    l2p = models.IntegerField(default=0)
    l3p = models.IntegerField(default=0)
    l4p = models.IntegerField(default=0)
    l5p = models.IntegerField(default=0)
    l6p = models.IntegerField(default=0)
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
    l7s = models.IntegerField(default=0)
    l8s = models.IntegerField(default=0)
    l9s = models.IntegerField(default=0)

    def AjaxUpdate(self, prepared, spent):
        if prepared is not None:
            self.l1p = prepared[0]
            self.l2p = prepared[1]
            self.l3p = prepared[2]
            self.l4p = prepared[3]
            self.l5p = prepared[4]
            self.l6p = prepared[5]
            self.l7p = prepared[6]
            self.l8p = prepared[7]
            self.l9p = prepared[8]
        if spent is not None:
            self.l1s = spent[0]
            self.l2s = spent[1]
            self.l3s = spent[2]
            self.l4s = spent[3]
            self.l5s = spent[4]
            self.l6s = spent[5]
            self.l7s = spent[6]
            self.l8s = spent[7]
            self.l9s = spent[8]
        self.save()
