import datetime
from django.db import models
from django.contrib.sessions.models import Session

class Lot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=False)
    openforbids = models.BooleanField(default=False)
    votecontrol = models.BooleanField(default=False)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    def save(self):
        snap = datetime.datetime.now()
        self.modified = snap
        if self.pk is None:
            self.created = snap
        super(Lot, self).save()
        
    def __unicode__(self):
        return u'Lot: %s' % self.name

        
class Bid(models.Model):
    lot = models.ForeignKey('Lot')
    amount = models.FloatField()
    session = models.ForeignKey(Session, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    def save(self):
        snap = datetime.datetime.now()
        self.modified = snap
        if self.pk is None:
            self.created = snap
        super(Bid, self).save()
                    
    def __unicode__(self):
        return u'Bid: %d' % self.id  