from rest_framework import generics
from .models import *
from .serializers import CitizenSerializer

class ProductList(generic.listCreateAPIView):
  queryset = Citizen.objects.all()
  serializer_class = CitizenSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
