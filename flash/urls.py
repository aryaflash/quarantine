from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('flash/customers/', views.CustomerList.as_view(), name = 'customerList'),
    path('flash/customers/<int:pk>/', views.CustomerDetail.as_view(), name = 'customerDetail'),
    path('flash/customers/staff/<str:place>/', views.AvailableStaff.as_view(), name = 'staffFilterbyplace'),
    path('flash/customers/staff/<str:place>/available/', views.AvailableStaffByTime.as_view(), name = 'stafffilterbytime'),
]