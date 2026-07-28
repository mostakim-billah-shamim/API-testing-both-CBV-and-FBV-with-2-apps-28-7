from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
