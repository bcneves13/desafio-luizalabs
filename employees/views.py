from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Employees


def index(request):
	return HttpResponse('DJango running on port 8000')
    

def list(request):
	return JsonResponse(list(Employees.objects.all()))


def create(request):
	print(list(Employees.objects.all()))
	return JsonResponse({'foo': 'data'})


def delete(request):
	print(list(Employees.objects.all()))
	return JsonResponse({'foo': 'data'})
