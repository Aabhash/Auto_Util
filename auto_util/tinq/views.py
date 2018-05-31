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

    # Get values for boxes that have been checked
    check_boxes = request.POST.getlist('schema_check')
    
    # For each schema checked, get tables from that schema
    tables = []
    for c in check_boxes:
        for t in (Schema_Info.objects.filter(table_schema=c)):
            tables.append(str(t))

    txt_o = ['No Input']
    txt_query = request.POST.get('txt_q')
    if  (tables != []) and (txt_query is not None):
        txt_o = operator.execute(tables, txt_query)

    context = {'schemas':schemas, 'output': txt_o}
    return render(request, 'tinq/index.html', context)

