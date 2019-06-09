from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.authtoken.models import Token

class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Employees.objects.all().order_by('-id')
    serializer_class = EmployeesSerializer

    @action(detail=True, methods=['get'])
    def list(self, request):
    	queryset = Employees.objects.all().order_by('id')
    	serializer = EmployeesSerializer(queryset, many=True)
    	return JsonResponse(serializer.data, safe=False)

    @action(detail=True, methods=['post'])	
    def create(self, request):
    	name = request.data.get('name', None)
    	email = request.data.get('email', None)
    	department = request.data.get('department', None)
    	if name is None or email is None or department is None:
    		return Response(status=422)

    	queryset = Employees.objects.create(name=name, email=email, department=department)

    	return Response(queryset.save())

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
    	queryset = get_object_or_404(Employees, pk=pk)
    	queryset.delete()
    	return JsonResponse({'message':'Employee deleted'})
	