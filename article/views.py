from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def create(request):
    return HttpResponse("<h3>Add Article</h3>")