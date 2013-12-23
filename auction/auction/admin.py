from django.contrib import admin
from auction.models import Bid, Lot

class LotAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class BidAdmin(admin.ModelAdmin):
    list_display = ('lot', 'biddername', 'amount',)
    
    
admin.site.register(Lot, LotAdmin)
admin.site.register(Bid, BidAdmin)