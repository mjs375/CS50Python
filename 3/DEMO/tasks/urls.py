from django.urls import path

from . import views

app_name="tasks" #helps uniquely ID all urls here (keeps from confusing Name-Space Collisions: if you have multiple apps and all have an "index"-named path, you need another identifier to say the "index.html" WITHIN this: "tasks")
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add") #use the 'name' for linking to this path 'add'
]
