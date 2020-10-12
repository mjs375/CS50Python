from django.shortcuts import render
from .models import Flight

# Create your views here.


def index(request):
    #Display a list of all Flight (objects)
        # remember the CONTEXT is a DICT{key:value, key:value}
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
        # "flights" is the variable name we give it to access in the html
        # Flight.objects.all() attaches the Python-Django for the variable
    })
