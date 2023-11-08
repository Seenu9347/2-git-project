from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chinni(request):
    return HttpResponse('<h1>hai anna</h1>')