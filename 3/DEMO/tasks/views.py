from django.shortcuts import render
from django import forms ####
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# tasks = [] #global variable available to entire APP [empty list for tasks]
    #updated each time form is submitted in add.html

class NewTaskForm(forms.Form): ####
    task = forms.CharField(label="New Task") #'name of task' field
#   priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
        #Put in BOTH client and server-side validation!

def index(request):
    if "tasks" not in request.session: #if you look inside the particular SESSION, and tasks is not there...:
        request.session["tasks"] = [] #create a LOCAL SESSION list of tasks
        # Run:
        # $ python3 manage.py migrate  [creates the DJANGO tables for storing data]
    #Render a page that displays a list of all tasks:
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] #right-hand value takes on value, L is variable HTML template has access to (making a dictionary: key-values)
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) #creates a blank form is () empty... otherwise request.POST submits all user's typed data in 'form' variable
        if form.is_valid(): #Check form is valid:
            task = form.cleaned_data["task"] #get task!
            request.session["tasks"] += [task] #tasks.append(task) DOESN'T work #add task to list of tasks
            return HttpResponseRedirect(reverse("tasks:index")) #figure out what the URL of the Tasks-Index is... smarter #Sends user back to index/homepage (list of tasks)
        else: #form is NOT valid:
            return render(request, "tasks/add.html", {
                "form": form #send back existing form data back to them
            })
    # else: if the user method="GET"-ed the page
    return render(request, "tasks/add.html", {
        "form": NewTaskForm() #context, gives template access to variable 'form' that is a NewTaskForm object

    })
