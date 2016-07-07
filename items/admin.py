from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers

from .models import (
        Category,
        Item,
        Price,
        Stock
        )

def update_all(modeladmin, request, queryset):
    queryset.update(price = 0)
update_all.short_description = "Update selected items"

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

    def activate(self, request, queryset):
        rows_updated = 0
        for d in queryset.values():
            if d['status'] == 1:
                rows_updated = queryset.update(status = 1)
                if rows_updated == 1:
                    message_bit = "1 Item was"
                else:
                    message_bit = "%s Items were " % rows_updated
        if rows_updated == 0:
            self.message_user ("Item is being active already.")
        else:
            self.message_user (request, "%s successfully updated. " % rows_updated)

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type = "application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    actions = [export_as_json, activate]


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