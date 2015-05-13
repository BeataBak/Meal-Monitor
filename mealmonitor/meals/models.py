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
    is_foundation_vegatable = models.BooleanField(default = False)

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

    def save(self, *args, **kwargs):
        """
        Overriden to automatically generate meal names, e.g. 'Meal #3'.
        """
        if not self.pk and not self.name:
            meal_count = Meal.objects.filter(date_ate__year=self.date_ate.year,
                                             date_ate__month=self.date_ate.month,
                                             date_ate__day=self.date_ate.day).count()

            self.name = 'Meal #{}'.format(meal_count + 1)

        super().save(*args, **kwargs)

    def total_net_carbs(self):
        """
        Returns the total amount of net carbs in grams in this meal.
        """
        total_net_carbs = 0
        for food_item in self.fooditemmeal_set.all():
            total_net_carbs += food_item.food_item.net_carbs*food_item.quantity/100
        return total_net_carbs

    def total_fat(self):
        """
        Returns the total amount of fat in grams in this meal.
        """
        total_fat = 0
        for food_item in self.fooditemmeal_set.all():
            total_fat += food_item.food_item.fat*food_item.quantity/100
        return total_fat

    def total_protein(self):
        """
        Returns the total amount of protein in grams in this meal.
        """
        total_protein = 0
        for food_item in self.fooditemmeal_set.all():
            total_protein += food_item.food_item.protein*food_item.quantity/100
        return total_protein

    def total_calories(self):
        """
        Returns the total amount of calories in kcal in this meal.
        """
        total_calories = 0
        for food_item in self.fooditemmeal_set.all():
            total_calories += food_item.food_item.calories*food_item.quantity/100
        return total_calories

    def total_foundation_carbs(self):
        """
        Returns the total amount of net carbs in grams in this meal from foundation vegatables.
        """
        total_foundation_carbs = 0
        for food_item in self.fooditemmeal_set.filter(food_item__is_foundation_vegatable = True):
            total_foundation_carbs += food_item.food_item.net_carbs*food_item.quantity/100
        return total_foundation_carbs


class FoodItemMeal(models.Model):
    """
    An intermediate model to store the amount of FoodItem in a Meal.
    """
    meal = models.ForeignKey(Meal)
    food_item = models.ForeignKey(FoodItem)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} -> {}, {}g'.format(self.meal, self.food_item, self.quantity)
