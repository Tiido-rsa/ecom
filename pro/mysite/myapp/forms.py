from django import forms
from .models import Item

class Itemform(forms.ModelForm):

    def clean_item_price(self):
        item_price = self.cleaned_data['item_price']
        if item_price < 0:
            raise forms.ValidationError('Item price cannot be negative')
        return item_price

    def clean_item_description(self):
        item_description = self.cleaned_data['item_description']
        item_name = self.cleaned_data['item_name']
        # if len(item_description) < 10:
        #     raise forms.ValidationError('Item description must be at least 10 characters long')
        if item_description == item_name:
            raise forms.ValidationError('Item description cannot be the same as item name')
        return item_description

    class Meta:
        model   = Item
        fields  = ['item_name', 'item_price', 'item_description', 'item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder': 'e.g. Pizza', 'required': True}),
            'item_price': forms.TextInput(attrs={'placeholder': 'e.g. 100', 'required': True}),
            'item_description': forms.TextInput(attrs={'placeholder': 'e.g. Yummy Pizza', 'required': True}),
            'item_image': forms.TextInput(attrs={'placeholder': 'e.g. https://example.com/image.jpg', 'required': True}),
        }