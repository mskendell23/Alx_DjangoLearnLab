from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookshelf(request):
    return HttpResponse("Welcome to this Library.")