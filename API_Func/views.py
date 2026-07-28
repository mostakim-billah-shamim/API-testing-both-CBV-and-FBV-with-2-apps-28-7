from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def BookPage(request, id=None):
    if request.method == "POST":
        is_many = isinstance(request.data, list)
        serializer = Bookserializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == "GET":

        if id is not None:
            try:
                book = BookModel.objects.get(id=id)
                serializer = Bookserializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except BookModel.DoesNotExist:
                return Response({"msg": "Book not Found"}, status=status.HTTP_404_NOT_FOUND)

        book = BookModel.objects.all()
        serializer = Bookserializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if id is None:
        return Response({"msg": "Book not Found"})

    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({"msg": "Book not Found"}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "PUT":
        serializer = Bookserializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = Bookserializer(book, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
    
        


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def StorePage(request, id=None):
    if request.method == "POST":
        is_many = isinstance(request.data, list)
        serializer = Storeserializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == "GET":

        if id is not None:
            try:
                store = StoreModel.objects.get(id=id)
                serializer = Storeserializer(store)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except StoreModel.DoesNotExist:
                return Response({"msg": "store not Found"}, status=status.HTTP_404_NOT_FOUND)

        store = StoreModel.objects.all()
        serializer = Storeserializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if id is None:
        return Response({"msg": "store not Found"})

    try:
        store = StoreModel.objects.get(id=id)
    except StoreModel.DoesNotExist:
        return Response({"msg": "store not Found"}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "PUT":
        serializer = Storeserializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = Storeserializer(store, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        store.delete()
        return Response({"msg":"Data Deleted"}, status=status.HTTP_200_OK)
    
        

         









# Create your views here.
