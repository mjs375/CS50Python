from django.shortcuts import render
from django.http import HttpResponse #imports the ability 'HttpResponse'

# Create your views here.
    # Each view is something the user sees:

def index(request): #represents HTTP request user made to access server
    #return HttpResponse("Hello, world!!!!")
    #Actual web content for "http://127.0.0.1:8000/hello/"
    return render(request, "hello/index.html") #render not a string but an entire HTML FILE!!!!!

def puddle(request):
    return HttpResponse("Hello, puddle!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
    #format string! substitutes in variables... capitalize() is a Python function allowed in an f-string.
    return render(request, "hello/greet.html", {
        "name": name.capitalize() #DICT variable: key-name, value-variable
    })
    #CONTEXT: provide all the variables you want to provide access to




## The above functions would necessarily include a LOT of HTML in the return string... let's separate the response/HTML from the Python:
