from django.contrib import admin
from auction.models import Bid, Lot

class LotAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class BidAdmin(admin.ModelAdmin):
    list_display = ('lot', 'get_bidder_name', 'amount',)
    def get_bidder_name(self, obj):
        if obj.session:
            return obj.session.get_decoded().get('name')
        else:
            return None
    get_bidder_name.short_description = 'bidder'
    
admin.site.register(Lot, LotAdmin)
admin.site.register(Bid, BidAdmin)