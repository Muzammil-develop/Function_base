from django.shortcuts import render
from .models import Store
from .api_file.serializer import StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view (['GET' , 'POST'])

def store_list (request):
    if request.method == "GET":
        store = Store.objects.all ()
        serializer = StoreSerializer (store , many=True)
        return Response (serializer.data)
    
    if request.method == 'POST':
        serializer = StoreSerializer (data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)




@api_view (['GET' , 'PUT' , 'DELETE'])
def store_detail_view (request , pk):
    if request.method == 'GET':
        try :
            store = Store.objects.get (pk = pk)
        except :
            return Response ({'Error' : 'Car not Found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer (store)
        return Response (serializer.data)
    
    if request.method == 'POST':
        store = Store.objects.get (pk = pk)
        serializer = StoreSerializer (store , data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
    if request.method == "DELETE":
        store = Store.objects.get (pk = pk)
        store.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
