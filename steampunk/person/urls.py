from django.contrib import admin
from django.urls import path

from .views import person_all

urlpatterns = [
    path('', person_all),
]