from rest_framework import serializers
from .models import PredictionValue


class PredictionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionValue
        fields = ('glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'age')