from django.db import models

class PredictionValue(models.Model):
    glucose = models.IntegerField(blank=False, null=False)
    blood_pressure = models.IntegerField(blank=False, null=False)
    skin_thickness = models.IntegerField(blank=False, null=False)
    insulin = models.IntegerField(blank=False, null=False)
    bmi = models.FloatField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    
