from django.urls import path
from .views import *

urlpatterns = [
    path('appointment/', AppointmentPage.as_view(), name='appointment'),
    path('appointmentu/<int:pk>/', AppointmentUpdatePage.as_view(), name='appointmentu'),

    path('medicalrecord/', MedicalRecordPage.as_view(), name='medicalrecord'),
    path('medicalrecordu/<int:pk>/', MedicalRecordUpdatePage.as_view(), name='medicalrecordu'),
]