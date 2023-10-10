from rest_framework import serializers
from .models import Citizen, Province

class CitizenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Citizen
    fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Province
    fields = '__all__'