from django.test import TestCase

from django.core.urlresolvers import reverse

from datetime import date, datetime



class MealViewTests(TestCase):
    def test_if_redirects_to_today(self):

        """
        Checks if '/' redirects to today's date
        """
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, date.today().isoformat())