from .models import Transaction, Services, Patient, Appointment
from rest_framework.serializers import ModelSerializer


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"



class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"



class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
