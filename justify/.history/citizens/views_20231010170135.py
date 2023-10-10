from rest_framework import generics
from .models import *
from .serializers import CitizenSerializer

class CitizenList(generics.ListCreateAPIView):
  queryset = Citizen.objects.all()
  serializer_class = CitizenSerializer

class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class CitizenList(generics.ListCreateAPIView):
  queryset = Citizen.objects.all()
  serializer_class = CitizenSerializer

class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
