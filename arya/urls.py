from django.urls import path 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('arya/managers/', views.ManagerList.as_view(), name = 'Managers_List'),
    path('arya/managers/profile/<int:pk>/', views.ManagerDetail.as_view(), name = 'Manager_Detail'),
    path('arya/staff/', views.StaffList.as_view(), name = 'Staff_List'),
    path('arya/staff/<int:pk>/', views.StaffDetail.as_view(), name = 'Staff_Detail'),
    path('arya/<int:pk>/staffundermanager/', views.StaffUnderManager.as_view(), name = 'StaffUnderManage'),
    path('users/', views.UserList.as_view(), name = 'User_List'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'User_Detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
