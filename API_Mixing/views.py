from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin



class PatientPage(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PatientUpdatePage(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






class DoctorPage(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = DoctorModel.objects.all()
    serializer_class= DoctorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DoctorUpdatePage(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = DoctorModel.objects.all()
    serializer_class=DoctorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

    
        
# Create your views here.
