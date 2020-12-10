from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from .models import  Athlete,Action
from .serializers import  AthleteSerializer,ActionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AthleteListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('athlete','action')


class ActionListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


