from django.contrib import admin

from .models import (
        Category,
        Item,
        Price,
        Stock
        )

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(Stock)