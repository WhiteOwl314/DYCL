from django.http import HttpResponse
from django.shortcuts import render
from .models import Gallery


def index(request):
    return HttpResponse("hello")
