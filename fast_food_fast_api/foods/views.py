from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Food, SignUp, LogIn
from .serializers import FoodSerializer, SignUpSerializer, LogInSerializer

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class SignView(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

class LogInView(viewsets.ModelViewSet):
    queryset = LogIn.objects.all()
    serializer_class = LogInSerializer