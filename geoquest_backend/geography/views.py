# geography/views.py
from rest_framework.generics import ListCreateAPIView

from .models import Continent, Country
from .serializers import ContinentSerializer, CountrySerializer


class ContinentList(ListCreateAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class CountryList(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
