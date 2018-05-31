from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from tinq.src import operator
from .models import Schema_Info

def get_schemas():
    return Schema_Info.objects.values('table_schema').distinct()
    
def index(request):
    schemas = get_schemas()
    context = {'schemas':schemas}
    return render(request, 'tinq/index.html', context)

def click(request):
    schemas = get_schemas()

    # Gets checkbox values that have been checked
    check_boxes = request.POST.getlist('schema_check')
    
    tables = []
    # For each schema checked, get tables from that schema 
    for c in check_boxes:
        ts = (Schema_Info.objects.all().filter(table_schema=c))
        for t in ts:
            tables.append(t)

    txt_o = ['No Input']
    txt_query = request.POST.get('txt_q')
    if  (tables and txt_query) is not None:
        txt_o = operator.execute(tables, txt_query)

    context = {'schemas':schemas, 'output': txt_o}
    return render(request, 'tinq/index.html', context)

