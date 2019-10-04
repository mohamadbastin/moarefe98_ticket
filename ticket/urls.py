# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', ProfileListView.as_view()),

]
