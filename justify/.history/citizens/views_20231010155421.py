from rest_framework import generic
from .models import *
from .serializers import CitizenSerializer

class ProductList(generic.listCreateAPIView):
  queryset = Citizen.objects.all()
