from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    context = {
        'title': 'Home Page',
        "description": "Welcome to the home page of the students app.",#
        'number': 123,
        "list1": [1, 2, 3, 4, 5],
        'dict1': {'name': 'John', 'age': 25},

    }

    return render(request, 'students/home.html', context)
