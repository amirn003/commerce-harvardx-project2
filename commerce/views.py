from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# def index(request):
#     return HttpResponse("Commerce Index")

def create(request):
    return render(request, "auctions/create.html")