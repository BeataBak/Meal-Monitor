from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'meals.views.home', name='home'),
    url(r'^(?P<date>\d{4}-\d{2}-\d{2})$', 'meals.views.meal_list', name='meal_list'),
    url(r'^meal_create/(?P<date>\d{4}-\d{2}-\d{2})$', 'meals.views.meal_create', name='meal_create'),
    url(r'^admin/', include(admin.site.urls)),
]
