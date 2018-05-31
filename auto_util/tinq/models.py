from django.db import models

class Operator(models.Model): 
    query = models.CharField(max_length = 50000)
    tables = models.CharField(max_length = 50000)
    output = models.CharField(max_length = 20000)

class Schema_Info(models.Model):
    table_schema = models.CharField(max_length = 200)
    table_name = models.CharField(max_length = 100)
    table_description = models.CharField(max_length = 5000)

    def __str__(self):
        return self.table_name