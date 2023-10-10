from rest_framework import generics
from .models import *
from .serializers import CitizenSerializer, ProvinceSerializer

class CitizenList(generics.ListCreateAPIView):
  queryset = Citizen.objects.all()
  serializer_class = CitizenSerializer

class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class ProvinceList(generics.ListCreateAPIView):
  queryset = Province.objects.all()
  serializer_class = ProvinceSerializer

class ProvinceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
