from django.contrib import admin

from .models import (
        Category,
        Item,
        Price,
        Stock
        )

def update_all(modeladmin, request, queryset):
    queryset.update(price = 0)
update_all.short_description = "Update selected items"

def activate(modeladmin, request, queryset):
    queryset.update(status = 1)
    print "status updated"
activate.short_description = "Activate selected items"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_updated')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'category_name',
                    'description',
                    'stock_amount',
                    'price_price',
                    'status',
                    'date_updated'
                    )
    search_fields = ('code', 'category__name', 'description')
    list_filter = ('category__name', 'date_created')
    actions = [activate]

class PriceAdmin(admin.ModelAdmin):
    list_display = (
                    'item_code',
                    'price',
                    'date_updated',
                    'user_name',
                    )
    search_fields = ('item__code', 'date_updated')
    list_filter = ('date_updated',)
    actions = [update_all]

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