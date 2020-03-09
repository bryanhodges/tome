from django.http import HttpResponse
from django.shortcuts import render
import re
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'home/homeTemplate.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )