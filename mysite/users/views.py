
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import ProfileSerializer      
from .models import Profile        