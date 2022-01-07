from django.db import models

class Trailinfo(models.Model):
    trailid = models.IntegerField(db_column='TrailID', primary_key=True)  # Field name made lowercase.
    trailname = models.CharField(db_column='TrailName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    popularity = models.FloatField(db_column='Popularity', blank=True, null=True)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    elevationgain = models.FloatField(db_column='ElevationGain', blank=True, null=True)  # Field name made lowercase.
    difficultyrating = models.IntegerField(db_column='DifficultyRating', blank=True, null=True)  # Field name made lowercase.
    routetype = models.CharField(db_column='RouteType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avgrating = models.FloatField(db_column='AvgRating', blank=True, null=True)  # Field name made lowercase.
    features = models.CharField(db_column='Features', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrailInformation'