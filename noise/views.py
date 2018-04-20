# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer
from django.http import Http404,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

# List all Sensors or create a new one
# Sensors/
class SensorList(APIView):

    def get(self,request):
        Sensors = Sensor.objects.all()
        serializer = SensorSerializer(Sensors,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDetail(APIView):
    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SensorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SensorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    all_sensors = Sensor.objects.all()
    context = {'all_sensors':all_sensors}
    return render(request,'noise/index.html',context)

def detail(request):
    all_sensors = Sensor.objects.all()
    context = {'all_sensors':all_sensors}
    return render(request,'noise/detail.html',context)

def home(request):
    return render(request,'noise/home.html')

def future(request):
    return render(request,'noise/future.html')

def team(request):
    return render(request,'noise/base.html')