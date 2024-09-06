from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=50)

class Services(models.Model):
    service_name = models.CharField(max_length=50)    
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    illness = models.CharField(max_length=60)
    required_service = models.ForeignKey(Services, on_delete=models.CASCADE)


