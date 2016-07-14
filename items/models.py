from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import intcomma

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 100)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class Item(models.Model):

    NEW = 0
    ACTIVE = 1
    UNACTIVE = 2

    STATUS_CHOICES = (
        (NEW, "New"),
        (ACTIVE, "Active"),
        (UNACTIVE, "Unactive")
    )

    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 20)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NEW)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def category_name(self):
        return self.category.name

    def stock_amount(self):
        stock = Stock()
        return stock.get_stock(self.id)

    def price_price(self):
        price = Price()
        price = round(float(price.get_price(self.id)), 2)
        return "IDR %s%s" % (intcomma(int(price)), ("%0.2f" % price)[-3:])

    def __str__(self):
        return self.code

class Stock(models.Model):
    amount = models.IntegerField()
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

    def item_code(self):
        return self.item.code

    def get_stock(self, id):
        stock = Stock.objects.filter(item_id=id).order_by('-id')
        if not stock:
            return 0
        else:
            return stock[0].amount

    def user_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    user_name.short_description = 'Updated By'

    def __str__(self):
        return str(self.amount)

class Price(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

    def item_code(self):
        return self.item.code

    def user_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def get_price(self, id):
        price = Price.objects.filter(item_id=id).order_by('-id')
        if not price:
            return 0
        else:
            return price[0].price

    user_name.short_description = 'Updated By'

    def __str__(self):
        return str(self.price)
