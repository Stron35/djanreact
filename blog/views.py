from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
	queryset = Lead.objects.all()
	serializer_class = LeadSerializer