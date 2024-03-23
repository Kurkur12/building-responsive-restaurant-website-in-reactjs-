from django.contrib import admin
from .models import RestaurantProfile, RestaurantFAQ, OpeningHour


@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ['day', 'opening_time', 'closing_time']

@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email']

@admin.register(RestaurantFAQ)
class RestaurantFAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']