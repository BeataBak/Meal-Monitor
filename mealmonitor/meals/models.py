from django.db import models


class FoodItem(models.Model):
    """
    Anything that is edible or drinkable. This could be a product
    (e.g. Hoegaarden beer) or an ingredient (e.g. chicken).
    """
    name = models.CharField(blank=True, max_length=128)
    net_carbs = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    calories = models.IntegerField()


class Meal(models.Model):
    """
    One or more food items eaten at a specific time. This does not
    have to adhere to the traditional defintion of a "meal"
    (e.g. breakfast), it could be just a snack.
    """
    name = models.CharField(blank=True, max_length=128)
    food_items = models.ManyToManyField(FoodItem, through='FoodItemMeal')
    date_ate = models.DateTimeField(auto_now_add=True)


class FoodItemMeal(models.Model):
    """
    An intermediate model to store the amount of FoodItem in a Meal.
    """
    meal = models.ForeignKey(Meal)
    food_item = models.ForeignKey(FoodItem)
    quantity = models.IntegerField()
