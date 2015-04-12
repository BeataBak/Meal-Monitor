from datetime import date, datetime

from django.shortcuts import render, redirect

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

    return render(request, 'meal_list.html', {'date': date, 'meals': meals})


def meal_create(request, date):
    """
    Creates a meal for `date`.

    Todo: in the future this will be a separate page.
    """
    date = datetime.strptime(date, '%Y-%m-%d').date()

    Meal.objects.create(date_ate=date)

    return redirect('meal_list', date=date)
