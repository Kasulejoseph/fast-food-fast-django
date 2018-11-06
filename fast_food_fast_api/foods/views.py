from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializer

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
