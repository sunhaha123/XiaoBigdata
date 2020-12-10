from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from .models import  Analysis,Curve_fit
from .serializers import  AnalysisSerializer,Curve_fitSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AnalysisListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('athlete','action')


class Curve_fitListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Curve_fit.objects.all()
    serializer_class = Curve_fitSerializer


