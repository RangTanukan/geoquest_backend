# geography/serializers.py
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Continent, Country

class ContinentSerializer(ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
