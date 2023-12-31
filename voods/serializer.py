from rest_framework import serializers
from .models import Vood

class VoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vood
        fields =['id', 'name', 'description']