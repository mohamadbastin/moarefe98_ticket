from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .serializers import *
# Create your views here.
from .models import *
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response


class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usr = self.request.user
        user = Profile.objects.filter(user=usr)
        return user
