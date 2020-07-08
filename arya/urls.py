from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('arya/managers/', views.ManagerList.as_view(), name = 'Managers List'),
    path('arya/managers/<int:pk>/', views.ManagerDetail.as_view(), name = 'Manager Detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
