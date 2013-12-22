from django.db import models

class Lot(models.Model):
    name = models.CharField()
    description = models.TextField()
    openforbids = models.BooleanField(default=False)
    votecontrol = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % self.name

        
class Bid(models.Model):
    lot = models.ForeignKey('Lot')
    amount = models.FloatField()
    biddername = models.CharField()
    
    def __unicode__(self):
        return u'Bid %'
    