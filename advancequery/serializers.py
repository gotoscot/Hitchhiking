from rest_framework import serializers
from .models import *


class UserRankingserializers(serializers.ModelSerializer):

    class Meta:
        model = UserRankingmodel
        fields = ['UserID', 'FirstName', 'LastName', 'VisitedTrails', 'Gender', 'Difficulty']

# class Recommendlistserializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Recommendlistmodel
#         fields = ['TrailName', 'State', 'DifficultyRating', 'AvgRating', 'Features']
