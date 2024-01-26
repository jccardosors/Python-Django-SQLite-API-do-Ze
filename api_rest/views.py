from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

import json

# Create your views here.

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        try:

            new_user = request.data
            serializer = UserSerializer(data=new_user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT'])
def upt_user(request):
    if request.method == 'PUT':
        try:
            nick_name = request.data['user_nickname']
            try:
                current_user = User.objects.get(pk=nick_name)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)            

            serializer = UserSerializer(current_user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)            

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def del_user(request):
    try:
        user_to_delete = User.objects.get(pk=request.data['user_nickname'])
        user_to_delete.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

