from django.shortcuts import render
from rest_framework import generics, serializers
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
