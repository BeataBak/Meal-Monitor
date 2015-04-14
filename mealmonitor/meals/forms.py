from django import forms

from .models import FoodItemMeal

class ItemForm(forms.ModelForm):

    class Meta:
        model = FoodItemMeal
        fields = ('meal', 'food_item', 'quantity')