from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    """
    Redirect the user to the meals list for today.
    """
    return redirect('meal_list', date=date.today().isoformat())


def meal_list(request, date):
    """
    Displays all the meals for a particular day.
    """
    return render(request, 'meal_list.html', {})
