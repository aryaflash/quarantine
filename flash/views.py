from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from arya.models import Staff
from arya.serializers import StaffSerializer
from django.utils import timezone
from rest_framework import permissions

# Create your views here.
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AvailableStaff(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, place):
        try:
            return Staff.objects.filter(town = place)
        except Staff.DoesNotExist:
            raise Http404

    def get(self, request, place):
        staff = self.get_object(place = place)
        serializer = StaffSerializer(staff, many = True)
        return Response(serializer.data)
        
class AvailableStaffByTime(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, place):
        try:
            return Staff.objects.filter(town = place).exclude(availableTill__lte = timezone.now())
        except Staff.DoesNotExist:
            raise Http404

    def get(self, request, place):
        print(timezone.now())
        staff = self.get_object(place = place)
        serializer = StaffSerializer(staff, many = True)
        return Response(serializer.data)
