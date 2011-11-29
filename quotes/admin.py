from quotes.models import Quote
from django.contrib import admin

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'nick', 'host', 'quote', 'added')
    list_filter = ['nick', 'host', 'channel']
    search_fields = ['nick','quote']
    date_hierarchy = 'added'
admin.site.register(Quote, QuoteAdmin)
