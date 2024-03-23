from django.shortcuts import render
from rest_framework import generics
from .models import Category, Menu
from .serializers import MenuSerializer, CategorySerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
