from django.shortcuts import render
from django.contrib import admin, messages
from django.contrib.admin import helpers
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
                    'stock_available',
                    'price_price',
                    'status',
                    'date_updated'
                    )
    search_fields = ('code', 'category__name', 'description')
    list_filter = ('category__name', 'date_created')

    def activate(self, request, queryset):
        active = 1
        counter = 0
        for data in queryset.values():
            if data['status'] != active:
                counter += 1
                rows_updated = queryset.update(status = active)
        if counter == 0:
            self.message_user (request, "Item is being active already.", level=messages.WARNING)
        else:
            self.message_user (request, "%s successfully updated. " % counter, level=messages.SUCCESS)

    def add_stock(self, request, queryset):

        from items.form import ItemForm

        if request.POST.get('post'):
            form = ItemForm(request.POST)

            print form
            # for data in queryset:
                # print data['stock_available'], data['id']

            # if form.is_valid():
            #     new_stock = form.cleaned_data['stock']
            #     updated = queryset.update(stock_available=new_stock)
            #     return
        else:
            form = ItemForm()

        formfield_overrides = {
            models.DecimalField: { 'widget': TextInput ( attrs= {'class': 'text-right' } ), }
        }

        context = {
                    'title': u'Add Stock',
                    'objects': queryset,
                    'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
                    'form': form
        }

        return render(request,
                      'admin/items/add_stock.html',
                      context
        )

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type = "application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    actions = [export_as_json, activate, add_stock]


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