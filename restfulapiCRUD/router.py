from employeeAPI.viewsets import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', EmployeeViewSet)
