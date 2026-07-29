from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = '__all__'



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'


