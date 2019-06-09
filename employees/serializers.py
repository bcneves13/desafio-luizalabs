from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.Serializer):
	class Meta:
		model = Employees
		fields = ('id', 'name', 'email', 'department')
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=200)
	email = serializers.EmailField(max_length=200)
	department = serializers.CharField(max_length=200)