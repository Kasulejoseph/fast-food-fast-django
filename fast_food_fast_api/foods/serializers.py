from rest_framework import serializers
from .models import Food, SignUp

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'  #include all model fields

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'username', 'email', 'password')