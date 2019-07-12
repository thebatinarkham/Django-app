from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publised',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable= ('is_publised',)
    search_fields=('title','description','address','price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
