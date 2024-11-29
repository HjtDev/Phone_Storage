from django.contrib import admin
from .models import Brand, Phone


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    list_editable = ('nationality',)
    search_fields = ('name', 'nationality')
    list_display_links = ('name',)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'color', 'display_size', 'made_in', 'is_available')
    list_editable = ('price', 'is_available')
    list_filter = ('is_available', 'brand')
    search_fields = ('brand__name', 'brand__nationality', 'model', 'color', 'display_size', 'made_in')
    autocomplete_fields = ('brand',)

