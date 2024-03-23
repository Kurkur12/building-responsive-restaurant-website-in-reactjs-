from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    RestaurantProfileSerializer, 
    OpeningHourSerializer, 
    RestaurantFAQSerializer
)
from .models import (
    RestaurantProfile,
    OpeningHour,
    RestaurantFAQ
)


class RestaurantProfileView(generics.ListAPIView):
    queryset = RestaurantProfile.objects.all()
    serializer_class = RestaurantProfileSerializer

class OpeningHourView(generics.ListAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHourSerializer

class RestaurantFAQView(generics.ListAPIView):
    queryset = RestaurantFAQ.objects.all()
    serializer_class = RestaurantFAQSerializer

