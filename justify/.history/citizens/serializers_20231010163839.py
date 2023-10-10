from rest_framework import serializers
from .models import Citizen, Province

class CitizenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Citizen
    fields = __all__