from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
#from src import operator

def index(request):
    context={}
#     #q = Operator.query
#     #t = Operator.tables
#     #output = operator.main
#     #context = {'query':q,'tables':t}
    return render(request, 'tinq/index.html', context)

def click(request):
    context= {}
    txt_tb = request.POST.get('txt_tb')
    txt_query = request.POST.get('txt_q')
    print(a)
    return render(request, 'tinq/index.html', context)

