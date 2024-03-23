from .models import OpeningHour, RestaurantFAQ, RestaurantProfile
from rest_framework import serializers


class OpeningHourSerializer(serializers.ModelSerializer):
    day = serializers.CharField(source='get_day_display')
    class Meta:
        model = OpeningHour
        fields = ["id", "day", "opening_time", "closing_time"]


class RestaurantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantProfile
        fields = [
            "id",
            "name",
            "logo",
            "about_us",
            "address",
            "phone",
            "email",
            "facebook",
            "instagram",
            "twitter",
        ]


class RestaurantFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantFAQ
        fields = ["id", "question", "answer"]
