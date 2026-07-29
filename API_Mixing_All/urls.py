from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('pharmacyitem', PharmacyItemPage, basename='pharmacyitem')

router.register('billinginvoice', BillingInvoicePage, basename='billinginvoice')

urlpatterns = [

    path('', include(router.urls)),
]