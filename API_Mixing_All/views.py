from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

class PharmacyItemPage(viewsets.ModelViewSet):
    queryset = PharmacyItemModel.objects.all()
    serializer_class = PharmacyItemSerializer


class BillingInvoicePage(viewsets.ModelViewSet):
    queryset = BillingInvoiceModel.objects.all()
    serializer_class = BillingInvoiceSerializer

# Create your views here.
