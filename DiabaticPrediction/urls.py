from django.urls import path
from . import views


urlpatterns = [
    path('prediction/',views.prediction,name='prediction'),
    path('fetch-news/',views.fetch_news,name='fetch_news'),
]