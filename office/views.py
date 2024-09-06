from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from office.models import Transaction, Patient, Services, Appointment
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

