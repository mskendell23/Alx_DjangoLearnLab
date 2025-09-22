from django.shortcuts import render
from django.http import HttpResponse

# Http Response
def api(request):
    return HttpResponse("Welcome to ADVANCED API.")
