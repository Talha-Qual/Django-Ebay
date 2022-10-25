from django.contrib import admin

from .models import *

admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Watchlist)
admin.site.register(User)