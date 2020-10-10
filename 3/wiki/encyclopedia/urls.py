from django.urls import path

from . import views

app_name="wiki" #Let's your call links like {% url "wiki:entries" %}

urlpatterns = [
    path("", views.index, name="index"),
    #INDEX/homepage

    path('wiki/', views.randomizer, name="random"),
    #path on any 'wiki/' page, calls randomizer() f(x) from views.py, gives it the reference name "random" to call (for linking, &c.)

    path('wiki/new', views.new, name="new"),

    #path('wiki/edit', views.edit, name="edit"),

    path("wiki/<str:title>", views.entry, name="entry")
    #makes wiki/"__" a string called title. Go into views file, use entry function, pass in 'title'.
    #Must be last, lest it overrides any other "wiki/[anything]" path-name

]
