from django.shortcuts import render
from django.http import HttpResponce

def index(request):
    return HttpResponce("Rango says hey there partner!")

