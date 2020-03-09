from django.http import HttpResponse
from django.shortcuts import render
import re
from datetime import datetime

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def hello_there(request, name):
    return render(
        request,
        'home/homeTemplate.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )