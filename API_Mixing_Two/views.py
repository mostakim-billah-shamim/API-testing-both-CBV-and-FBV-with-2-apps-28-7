from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class AppointmentPage( ListCreateAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentUpdatePage(RetrieveUpdateDestroyAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer



class MedicalRecordPage(ListCreateAPIView):
    queryset = MedicalRecordModel.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordUpdatePage(RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecordModel.objects.all()
    serializer_class = MedicalRecordSerializer





# Create your views here.
