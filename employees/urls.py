from django.urls import path
from .views import EmployeesViewSet

urlpatterns = [
    path('',EmployeesViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee'),
    path('<int:pk>', EmployeesViewSet.as_view({'delete': 'delete'}), name='delete-employee'),
]