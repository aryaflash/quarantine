from rest_framework import serializers
from .models import Manager, Staff
from django.contrib.auth.models import User

class ManagerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Manager
        fields = ['name', 'gmail', 'phoneNumber', 'address', 'password', 'town', 'state', 'owner']

class StaffSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Staff
        fields = ['name', 'services', 'gmail', 'phoneNumber', 'address', 'manager', 'town', 'state', 'availableFrom', 'availableTill', 'password', 'owner']

class UserSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(many = True, queryset = Manager.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'manager']
