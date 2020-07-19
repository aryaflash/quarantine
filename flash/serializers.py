from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'gmail', 'phoneNumber', 'address', 'password', 'town', 'state']
