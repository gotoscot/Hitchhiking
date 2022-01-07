from rest_framework import serializers
from .models import *


class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailinfo
        fields = '__all__'
