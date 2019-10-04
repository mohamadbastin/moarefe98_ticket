from django.shortcuts import render
from .serializers import *
# Create your views here.
from .models import *
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response


class SeatListView(ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        ls = []
        ob = Seat.objects.all()
        tmp = []
        blln = Seat.objects.last()

