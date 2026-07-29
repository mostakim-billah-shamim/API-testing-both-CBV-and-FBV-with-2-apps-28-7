from rest_framework import serializers
from .models import *


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = '__all__'



class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecordModel
        fields = '__all__'


