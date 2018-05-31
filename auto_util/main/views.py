from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

def home(request):
    return render(request, 'main/home.html')