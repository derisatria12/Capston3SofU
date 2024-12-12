from django import forms

from .models import Category, Item

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class ItemForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}))
    class Meta:
        model = Item
        fields = ['category', 'item_title', 'description', 'price', 'image', 'is_available']
    