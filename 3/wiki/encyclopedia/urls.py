from django.urls import path

from . import views

app_name="wiki" #Let's your call links like {% url "wiki:entries" %}

urlpatterns = [
    path("", views.index, name="index"),
    # INDEX/homepage path "/"
    # Look in views.py, function index() to execute

    path('wiki/', views.randomizer, name="random"),
    #path on any 'wiki/' page, calls randomizer() f(x) from views.py, gives it the reference name "random" to call (for linking, &c.)

    path('wiki/search', views.search, name="search"),

    path('wiki/new', views.new, name="new"),

    path('wiki/edit/<str:title>', views.edit, name="edit"),

    path("wiki/<str:title>", views.entry, name="entry"),
    # Makes wiki/"__" a string called title. Go into views file, use entry function, pass in 'title'.
    # Must be last, lest it overrides any other "wiki/[anything]" path-name





    #path("<str:falsetitle>", views.bad_entry)
    # if none of the above path-names are satisfied, it is probably a path-name
    # that does not exist (user trying to go to a page manually).

]
