from django.test import TestCase

from django.core.urlresolvers import reverse

from datetime import date, datetime
from .models import Meal, FoodItem, FoodItemMeal


class MealViewTests(TestCase):
    def test_if_redirects_to_today(self):
        """
        Checks if '/' redirects to today's date
        """
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, date.today().isoformat())


class MealModelTests(TestCase):
    def setUp(self):
        self.food_item = FoodItem.objects.create(
            name='food',
            net_carbs=17,
            fat=33,
            protein=27,
            calories=473,
        )

    def test_auto_meal_names(self):
        """
        If no meal name is provided does one automatically get
        assigned? e.g. Meal #1, Meal #2 etc.
        """
        meal_names = []

        for meal_num in range(1, 11):
            meal_names.append('Meal #{}'.format(meal_num))
            Meal.objects.create(date_ate = date.today())

        self.assertListEqual(meal_names, [m.name for m in Meal.objects.all()])

    def test_no_auto_meal_names(self):
        """
        If a meal name is provided it should not auto generate a
        "Meal #1" type name.
        """
        Meal.objects.create(name='Breakfast', date_ate=date.today())
        self.assertEquals(Meal.objects.all()[0].name, 'Breakfast')

    def test_total_net_carbs(self):
        """
        Does the `total_net_carbs` method work correctly?
        """
        meal = Meal.objects.create(name='Breakfast', date_ate=date.today())

        for food_num in range(1, 5):
            FoodItemMeal.objects.create(meal=meal, food_item=self.food_item, quantity=100)

        self.assertEquals(meal.total_net_carbs(), 68)

    def test_total_fat(self):
        """
        Does the `total_fat` method work correctly?
        """

        meal = Meal.objects.create(name='Breakfast', date_ate=date.today())

        for food_num in range(1, 5):
            FoodItemMeal.objects.create(meal=meal, food_item=self.food_item, quantity=100)

        self.assertEquals(meal.total_fat(), 132)

    def test_total_protein(self):
        """
        Does the `total_protein` method work correctly?
        """

        meal = Meal.objects.create(name='Breakfast', date_ate=date.today())

        for food_num in range(1, 5):
            FoodItemMeal.objects.create(meal=meal, food_item=self.food_item, quantity=100)

        self.assertEquals(meal.total_protein(), 108)

    def test_total_calories(self):
        """
        Does the `total_protein` method work correctly?
        """

        meal = Meal.objects.create(name='Breakfast', date_ate=date.today())

        for food_num in range(1, 5):
            FoodItemMeal.objects.create(meal=meal, food_item=self.food_item, quantity=100)

        self.assertEquals(meal.total_calories(), 1892)
        pass

    def test_total_foundation_carbs(self):
        """
        Does the `total_foundation_carbs` method work correctly?
        """
        meal = Meal.objects.create(name='Breakfast', date_ate=date.today())

        for food_num in range(1, 5):
            FoodItemMeal.objects.create(meal=meal, food_item=self.food_item, quantity=100)

        self.assertEquals(meal.total_foundation_carbs(), 0)