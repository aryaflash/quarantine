from .serializers import ManagerSerializer, StaffSerializer
from .models import Manager, Staff
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
# Create your views here.

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffUnderManager(APIView):
    def get_object(self, pk):
        try:
            m = Manager.objects.get(pk = pk)
            try:
                return m.staffMembers.all()
            except Staff.DoesNotExist:
                raise Http404
        except Manager.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        staff = self.get_object(pk = pk)
        serializer = StaffSerializer(staff, many = True)
        return Response(serializer.data)    