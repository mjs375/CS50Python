from django.urls import path #gives ability to reroute urls
from . import views #imports any functions we've created in views.py
    # "from ." means from current directory


urlpatterns = [
    path("", views.index, name="index"), #optional name makes referencing easy

    path("puddle", views.puddle, name="puddle"),
    #url path, function to run (from views.py), and an optional name for referencing)

    path("<str:name>", views.greet, name="greet")
    #This route can be ANY string (any name we enter), it will call the greet function and pass the name as a parameter.
    #"/<name>"


]
# ^^List of all URL patterns a user might visit while using our site
