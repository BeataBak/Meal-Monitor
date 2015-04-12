from django.db import models


class FoodItem(models.Model):
    """
    Anything that is edible or drinkable. This could be a product
    (e.g. Hoegaarden beer) or an ingredient (e.g. chicken).
    """
    name = models.CharField(blank=True, max_length=128)
    net_carbs = models.FloatField(help_text='per 100g')
    fat = models.FloatField(help_text='per 100g')
    protein = models.FloatField(help_text='per 100g')
    calories = models.IntegerField(help_text='per 100g')

    def __str__(self):
        return self.name


class Meal(models.Model):
    """
    One or more food items eaten at a specific time. This does not
    have to adhere to the traditional defintion of a "meal"
    (e.g. breakfast), it could be just a snack.
    """
    name = models.CharField(blank=True, max_length=128)
    food_items = models.ManyToManyField(FoodItem, through='FoodItemMeal')
    date_ate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def total_net_carbs(self):
        """
        Returns the total amount of net carbs in grams in this meal.
        """
        total_net_carbs = 0
        for food_item in self.food_items.all():
            total_net_carbs += food_item.net_carbs
        return total_net_carbs

    def total_fat(self):
        """
        Returns the total amount of fat in grams in this meal.
        """
        total_fat = 0
        for food_item in self.food_items.all():
            total_fat += food_item.fat
        return total_fat

    def total_protein(self):
        """
        Returns the total amount of protein in grams in this meal.
        """
        total_protein = 0
        for food_item in self.food_items.all():
            total_protein += food_item.protein
        return total_protein

    def total_calories(self):
        """
        Returns the total amount of calories in kcal in this meal.
        """
        total_calories = 0
        for food_item in self.food_items.all():
            total_calories += food_item.calories
        return total_calories


class FoodItemMeal(models.Model):
    """
    An intermediate model to store the amount of FoodItem in a Meal.
    """
    meal = models.ForeignKey(Meal)
    food_item = models.ForeignKey(FoodItem)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} -> {}, {}g'.format(self.meal, self.food_item, self.quantity)
