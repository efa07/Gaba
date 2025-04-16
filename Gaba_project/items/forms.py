from django import forms
from .models import Item

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'image','price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),
            'category': forms.Select(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),   
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),
            'price': forms.NumberInput(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full border border-gray-300 rounded-md shadow-sm p-2'}),
        }

