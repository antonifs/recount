from django import forms
from items.models import *

class ItemForm(forms.Form):
    stock_available = forms.CharField()