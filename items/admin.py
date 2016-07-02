from django.contrib import admin

from .models import (
        Category,
        Item,
        Price,
        Stock
        )

def update_price(modeladmin, request, queryset):
    queryset.update(status = 2)
update_price.short_description = "Update Price"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_updated')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'category_name',
                    'description',
                    'stock_amount',
                    'user_name',
                    'date_updated'
                    )
    search_fields = ('code', 'category__name', 'description')
    list_filter = ('category__name', 'date_created')
    actions = [update_price]

class PriceAdmin(admin.ModelAdmin):
    list_display = (
                    'item_code',
                    'price',
                    'date_updated',
                    'user_name',
                    )
    search_fields = ('item__code', 'date_updated')
    list_filter = ('date_updated',)

class StockAdmin(admin.ModelAdmin):
    list_display = (
                    'item_code',
                    'amount',
                    'date_updated',
                    'user_name',
                    )
    search_fields = ('item__code', 'date_updated')
    list_filter = ('date_updated',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Stock, StockAdmin)