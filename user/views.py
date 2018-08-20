from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,"register.html")

def loginUser(request):
    return render(request,"login.html")


def logoutUser(request):
    pass