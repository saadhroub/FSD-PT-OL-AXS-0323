from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hi, I come from the sales app")