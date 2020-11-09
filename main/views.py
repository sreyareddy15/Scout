from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
# Create your views here.


def dashboard(request):
    # return HttpResponse("Something")
    return render(request, "main/home.html", context={})


def stage(request, stage_num):
    return render(request, "main/stage.html")
