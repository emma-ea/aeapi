from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from . import serializers, models

# Create your views here.
def index(request):
    return HttpResponse("pass image to predict age")


class APViewSet(viewsets.ModelViewSet):
    queryset = models.AgePrediction.objects.all().order_by("uid")
    serializer_class = serializers.APSerializer

