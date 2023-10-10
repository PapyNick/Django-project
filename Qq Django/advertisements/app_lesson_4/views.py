from django.shortcuts import render
from django.http import HttpResponse

def lesson(request):
    return HttpResponse('Домашка по 4 занятию')

# Create your views here.
