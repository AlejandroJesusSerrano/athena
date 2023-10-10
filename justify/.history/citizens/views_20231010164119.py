from rest_framework import generics
from .models import *
from .serializers import CitizenSerializer

class ProductList(generics.ListCreateAPIView):
  queryset = Citizen.objects.all()
  serializer_class = CitizenSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
