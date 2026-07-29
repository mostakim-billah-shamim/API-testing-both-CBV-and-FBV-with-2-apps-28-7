from rest_framework import serializers
from .models import *



class PharmacyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyItemModel
        fields = '__all__'



class BillingInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInvoiceModel
        fields = '__all__'


