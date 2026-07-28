from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *



class StudentPage(APIView):

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = StudentSerializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(serlf, request, id=None):
        if id is not None:
            try:
                student = StudentModel.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except StudentModel.DoesNotExist:
                return Response({'msg':'Student Not Found'}, status=status.HTTP_404_NOT_FOUND)

        student= StudentModel.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        student = StudentModel.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer. errors, status=status.HTTP_404_NOT_FOUND)


    def patch(seld, request, id):
        student = StudentModel.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer. errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        student = StudentModel.objects.get(id=id)
        student.delete()
        return Response({'msg':'Student data Deleted'}, status=status.HTTP_200_OK)



class TeacherPage(APIView):

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = TeacherSerializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(serlf, request, id=None):
        if id is not None:
            try:
                teacher = TeacherModel.objects.get(id=id)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TeacherModel.DoesNotExist:
                return Response({'msg':'teacher Not Found'}, status=status.HTTP_404_NOT_FOUND)

        teacher= TeacherModel.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        teacher = TeacherModel.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer. errors, status=status.HTTP_404_NOT_FOUND)


    def patch(seld, request, id):
        teacher = TeacherModel.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer. errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        teacher = TeacherModel.objects.get(id=id)
        teacher.delete()
        return Response({'msg':'teacher data Deleted'}, status=status.HTTP_200_OK)




        
    


# Create your views here.
