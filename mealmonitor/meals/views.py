from .forms import ItemForm

from datetime import date, datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Meal


def home(request):
    """
    Redirect the user to the meals list for today.
    """
    return redirect('meal_list', date=date.today().isoformat())


def meal_list(request, date):
    """
    Displays all the meals for a particular day.
    """
    date = datetime.strptime(date, '%Y-%m-%d').date()

    # get all the meals eaten on this particular day
    meals = Meal.objects.filter(date_ate__year=date.year,
                                date_ate__month=date.month,
                                date_ate__day=date.day)

    return render(request, 'meal_list.html',
        {
            'date': date,
            'meals': meals,
            'food_item_form': ItemForm(),
            'daily_total_carbs': daily_total_carbs(meals),
            'daily_total_protein': daily_total_protein(meals),
            'daily_total_fat': daily_total_fat(meals),
            'daily_total_calories': daily_total_calories(meals),
            'daily_total_foundation_carbs': daily_total_foundation_carbs(meals),
            'daily_total_carbs_percentage': daily_total_carbs_percentage(meals),
            'daily_total_protein_percentage': daily_total_protein_percentage(meals),
            'daily_total_fat_percentage': daily_total_fat_percentage(meals),
        }
    )


def meal_create(request, date):
    """
    Creates a meal for `date`.

    Todo: in the future this will be a separate page.
    """
    date = datetime.strptime(date, '%Y-%m-%d').date()

    Meal.objects.create(date_ate=date)

    return redirect('meal_list', date=date)


def add_food_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def daily_total_carbs(meals):

    daily_total_carbs = 0

    for meal in meals:
        daily_total_carbs += meal.total_net_carbs()
    return daily_total_carbs

def daily_total_carbs_percentage(meals):
    try:
        daily_carbs_percentage = daily_total_carbs(meals) * 4.00/daily_total_calories(meals)
    except ZeroDivisionError:
        return 0

    return daily_carbs_percentage*100


def daily_total_protein(meals):

    daily_total_protein = 0

    for meal in meals:
        daily_total_protein += meal.total_protein()
    return daily_total_protein

def daily_total_protein_percentage(meals):
    try:
        daily_protein_percentage = daily_total_protein(meals) * 4.00/daily_total_calories(meals)
    except ZeroDivisionError:
        return 0

    return daily_protein_percentage*100

def daily_total_fat(meals):

    daily_total_fat = 0

    for meal in meals:
        daily_total_fat += meal.total_fat()
    return daily_total_fat

def daily_total_fat_percentage(meals):
    try:
        daily_fat_percentage = daily_total_fat(meals) * 9.00/daily_total_calories(meals)
    except ZeroDivisionError:
        return 0

    return daily_fat_percentage*100

def daily_total_calories(meals):

    daily_total_calories = 0

    for meal in meals:
        daily_total_calories += meal.total_calories()
    return daily_total_calories

def daily_total_foundation_carbs(meals):

    daily_total_foundation_carbs = 0

    for meal in meals:
        daily_total_foundation_carbs += meal.total_foundation_carbs()
    return daily_total_foundation_carbs