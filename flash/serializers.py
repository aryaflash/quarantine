from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Customer
        fields = ['name', 'gmail', 'phoneNumber', 'address', 'password', 'town', 'state', 'owner']
        
