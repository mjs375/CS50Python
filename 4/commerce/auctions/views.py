from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

    #import Class-es from models.py:
from .models import User, Listing, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all() #pull all listing objects and make accessible to index.html
    })


def login_view(request):
    if request.method == "POST": #form submitted w/ credentials

        # Attempt to sign user in
        username = request.POST["username"] #get username from form
        password = request.POST["password"] # ditto
        user = authenticate(request, username=username, password=password) #check if valid user

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else: #bring user to the login form page:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



# DISPLAY INDIVIDUAL LISTING:
@login_required #decorator: a user must be logged-in to view the page
def listing(request, listing_id): #
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })














"""
https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
^^^ Django Documentation for ModelForms
"""
class NewListingForm(forms.ModelForm): #creating a ModelForm subclass
    class Meta: #configures the model to work from
        model = Listing
        # fields = '__all__' #pulls all fields from the model to use
        # exclude = ['owner'] #excludes a particular field from the model (while including all others)

        fields = ['title', 'desc', 'startbid','owner', 'image'] #list of form fields, pulled from model 'Listing'

        labels = { # DICT
            'title': 'Title',
            'desc': 'Description of Item',
            'startbid': 'Starting Bid',
            'owner': 'Owner',
            'image': 'Item Image URL'
        }
        widgets = {
            'title': forms.TextInput(), #this is actually the default
            'desc': forms.Textarea(),
            'startbid': forms.NumberInput(),
            'owner': forms.HiddenInput(), #because Listing poster shouldn't be able to 'choose owner', owner must always be them.

            #'image': forms.URLInput()


        }
#
# #
# # #
# #
#
@login_required
# CREATE A NEW LISTING:
def new(request):
    if request.method == "GET": # give the user
        return render(request, "auctions/new.html", {
            "form": NewListingForm(initial={'owner': request.user}) # creates an empty NewListingForm to display. Owner should automatically be set to 'request.user' and form should not allow that to be changed!
        })
    else: #POST:
        form = NewListingForm(request.POST) #create form instance from POST data
        if form.is_valid():
            form.save() #save a new Listing object from the form's data
            return index(request)
        else:
            return render(request, "auctions/index.html", {
                "message": "Listing posting failed.",
                "listings": Listing.objects.all()
                })



#
