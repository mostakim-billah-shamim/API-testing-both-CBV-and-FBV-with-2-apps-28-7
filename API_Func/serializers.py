from rest_framework import serializers
from .models import *



class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'



class Storeserializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'

