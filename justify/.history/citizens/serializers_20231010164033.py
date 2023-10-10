from rest_framework import serializers
from .models import Citizen, Province

class CitizenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Citizen
    fields = ('names', 'last_names', 'email', 'dni', 'cuil', 'province', 'location', 'address', 'created_at')