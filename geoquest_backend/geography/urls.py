# geography/urls.py
from django.urls import path
from .views import ContinentList, CountryList

urlpatterns = [
    path('continents/', ContinentList.as_view(), name='continent-list'),
    path('countries/', CountryList.as_view(), name='country-list'),
]
