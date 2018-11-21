from rest_framework import serializers
from .models import Food, SignUp, LogIn

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'username', 'email', 'password')

    def validate_username(self, username):
        name = SignUp.objects.filter(username__iexact=username)
        if name.exists():
            raise serializers.ValidationError("Username already taken, choose another username")
        return username


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogIn
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    # user = SignUpSerializer(many=True)
    class Meta:
        model = Food
        fields = '__all__'  #include all model fields
