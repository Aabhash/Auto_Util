from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from tinq.src import operator

def main(request):
    return render(request, 'tinq/main.html')

def index(request):
    return render(request, 'tinq/index.html')

def click(request):
    context= {}
    txt_o = ''
    txt_tb = request.POST.get('txt_tb')
    txt_query = request.POST.get('txt_q')
    txt_o = operator.execute(txt_tb, txt_query)
    context = {'output': txt_o}
    return render(request, 'tinq/index.html', context)

