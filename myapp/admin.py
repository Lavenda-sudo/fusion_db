from django.contrib import admin
from myapp.models import Products

admin.site.site_title="GID Shop"
admin.site.site_header="Shop MIS"
admin.site.site_title="Shop MIS Administration"

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'category', 'for_sale')
    search_fields = ('name', 'code', 'category')
    list_filter = ('category', 'for_sale')
    ordering = ('name', '-price')
