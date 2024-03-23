from django.urls import path
from .views import (
    RestaurantProfileView,
    OpeningHourView,
    RestaurantFAQView,
)


urlpatterns = [
    path("profile/", RestaurantProfileView.as_view()),
    path("opening-hour/", OpeningHourView.as_view()),
    path("faq/", RestaurantFAQView.as_view()),
]
