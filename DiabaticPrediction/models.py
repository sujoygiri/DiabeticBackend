from django.db import models

class PredictionValue(models.Model):
    glucose = models.IntegerField(blank=False, null=False, max_length=4)
    blood_pressure = models.IntegerField(blank=False, null=False, max_length=4)
    skin_thickness = models.IntegerField(blank=False, null=False, max_length=4)
    insulin = models.IntegerField(blank=False, null=False, max_length=4)
    bmi = models.FloatField(blank=False, null=False, max_length=4)
    age = models.IntegerField(blank=False, null=False, max_length=3)
    
