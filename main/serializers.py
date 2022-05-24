
from rest_framework import serializers
from .models import Todo_items
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo_items
        fields = '__all__'

   


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','first_name', 'last_name', 'email']


    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
