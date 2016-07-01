from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 100)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 20)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def category_name(self):
        return self.category.name

    def stock_amount(self):
        stock = Stock()
        return stock.get_stock(self.id)

    def user_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

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
        return stock[0].amount

    def __str__(self):
        return str(self.amount)

class Price(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

    def item_code(self):
        return self.item.code

    def __str__(self):
        return str(self.price)
