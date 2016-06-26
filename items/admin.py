from django.contrib import admin

from .models import (
        Category,
        Item,
        Price,
        Stock
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_updated')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'category_name', 'description', 'user_name', 'date_created', 'date_updated')
    search_fields = ('code', 'description')
    list_filter = ('category__name', 'date_created')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'date_updated')

class StockAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date_updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Stock, StockAdmin)