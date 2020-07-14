from rest_framework import serializers
from .models import Manager, Staff

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['name', 'gmail', 'phoneNumber', 'address', 'password']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['name', 'gmail', 'phoneNumber', 'address', 'manager']
