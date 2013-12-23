from django.db import models
from django.contrib.sessions.models import Session

class Lot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=False)
    openforbids = models.BooleanField(default=False)
    votecontrol = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % self.name

        
class Bid(models.Model):
    lot = models.ForeignKey('Lot')
    amount = models.FloatField()
    session = models.ForeignKey(Session, blank=True, null=True)
    
    def biddername(self):
        if self.session:
            return self.session.get_decoded().get('name')
        else:
            return None
            
    def __unicode__(self):
        return u'Bid %'