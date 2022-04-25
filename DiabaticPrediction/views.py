from .serializer import PredictionValueSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from decouple import config

from pathlib import Path
import joblib
import numpy as np

script_loacation = Path(__file__).absolute().parent
model_location = script_loacation / './assets/Diabetes_prediction_ml_model.cls'

# model = joblib.load(model_location)
# user_data = np.asarray((149,68,29,127,29.3,22))
# reshaped_user_data = user_data.reshape(1,-1)
# print(model.predict(reshaped_user_data))

@api_view(['POST'])
def prediction(request):
    if request.method == 'POST':
        serializer = PredictionValueSerializer(data=request.data)
        if serializer.is_valid():
            glucose = serializer.data.get('glucose')
            blood_pressure = serializer.data.get('blood_pressure')
            skin_thickness = serializer.data.get('skin_thickness')
            insulin = serializer.data.get('insulin')
            bmi = serializer.data.get('bmi')
            age = serializer.data.get('age')
            user_data = np.asarray((glucose,blood_pressure,skin_thickness,insulin,bmi,age))
            reshaped_user_data = user_data.reshape(1,-1)
            model = joblib.load(model_location)
            result = model.predict(reshaped_user_data)
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_news(request):
    if request.method == 'GET':
        URL = 'https://newsapi.org/v2/top-headlines'
        PARAMS = {'country':'in', 'category':'health', 'apiKey': config('NEWS_API_KEY')}
        r = requests.get(url = URL, params = PARAMS) 
        response = r.json() 
        return Response(response['articles'])
    return Response(status=status.HTTP_400_BAD_REQUEST)