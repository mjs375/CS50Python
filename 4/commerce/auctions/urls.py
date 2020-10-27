from django.urls import path

from . import views

urlpatterns = [
    #path("url-path-name", views.fuction-name, name="name-you-can-call"),

    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("<int:listing_id>", views.listing, name="listing"),

    path("new", views.new, name="new"),

    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watch/<int:listing_id>", views.add_watch, name="add_watch"),
    path("remove_watch/<int:listing_id>", views.remove_watch, name="remove_watch"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("bid/<int:listing_id>", views.bid, name="bid"),

    path("close/<int:listing_id>", views.close, name="close"), #Close an auction listing
    path("index2", views.index2, name="index2"), ########

    path("cat", views.cats, name="cats"),
    path("cat/<str:cat>", views.cat, name="cat")


]
