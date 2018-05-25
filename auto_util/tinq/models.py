from django.db import models

class Operator(models.Model): 
    query = models.CharField(max_length = 50000)
    tables = models.CharField(max_length = 50000)
    output = models.CharField(max_length = 20000)
