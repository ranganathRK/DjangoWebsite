
from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, "home.html", {"name":"Ranganath k"})

def about(request):
    return render(request, "about.html")
