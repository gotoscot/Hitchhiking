from django.db import models

class UserRankingmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    VisitedTrails = models.IntegerField()
    UserID = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Difficulty = models.FloatField()

class Recommendlistmodel(models.Model):
    TrailName = models.CharField(max_length=150)
    State = models.CharField(max_length=2)
    DifficultyRating = models.IntegerField()
    AvgRating = models.FloatField()
    Features = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)

# class Restaurant(models.Model):
#     RestaurantID = models.IntegerField(db_column="RestaurantID", primary_key=True)
#     RestaurantName = models.CharField(db_column="RestaurantName", max_length=100, blank=True, null=True)
#     Address = models.CharField(db_column="Address", max_length=255, blank=True, null=True)
#     City = models.CharField(db_column="City", max_length=50, blank=True, null=True)
#     State = models.CharField(db_column="State", max_length=10, blank=True, null=True)
#     PostalCode = models.IntegerField(db_column="PostalCode", blank=True, null=True)
#     Rating = models.floatField(db_column="Rating", blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'restaurant'
