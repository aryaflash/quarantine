from .serializers import ManagerSerializer, StaffSerializer, UserSerializer
from .models import Manager, Staff
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StaffUnderManager(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

