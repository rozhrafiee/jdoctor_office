from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=50)
    def __str__ (self):
        return self.date

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField() 
    def __str__ (self):
        return self.service_name
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    illness = models.CharField(max_length=60)
    required_service = models.ForeignKey(Services, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    def __str__ (self):
        return self.patient

