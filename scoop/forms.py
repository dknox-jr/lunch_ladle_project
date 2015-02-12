from django import forms
from models import Item, Ingredient, User
from django.contrib.admin.widgets import FilteredSelectMultiple


class ItemForm(forms.ModelForm):
    brand = forms.CharField(max_length=50, help_text="Brand Name")
    manufacturer = forms.CharField(max_length=50, help_text="Manufacturer/Producer")
    product_name = forms.CharField(max_length=100, help_text="Item/Product Name")
    item_code = forms.CharField(max_length=50, help_text="Product/UPC Code")
    item_category = forms.CharField(max_length=255, help_text="xItem/Product Category")
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=FilteredSelectMultiple(verbose_name="Ingredients", is_stacked=False))
    nutritional_info = forms.CharField(max_length=255, help_text="Nutritional Information")
    allergen_info = forms.CharField(max_length=100, help_text="Allergen Information")
    item_price = forms.CharField(max_length=10, help_text="Price")

    class Meta:
        model = Item

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n',)


class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']