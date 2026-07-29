from django.urls import path
from .views import *

urlpatterns = [
    path('patient/', PatientPage.as_view(), name='patient'),
    path('patientu/<int:pk>/', PatientUpdatePage.as_view(), name='patientu'),

    path('doctor/', DoctorPage.as_view(), name='doctor'),
    path('doctoru/<int:pk>/', DoctorUpdatePage.as_view(), name='doctoru'),
]