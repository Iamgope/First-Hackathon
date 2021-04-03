from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_img','Tag',]
        