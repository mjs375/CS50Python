from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("<int:listing_id>", views.listing, name="listing"),

    path("new", views.new, name="new"),

    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watch/<int:listing_id>", views.add_watch, name="add_watch"),
    path("remove_watch/<int:listing_id>", views.remove_watch, name="remove_watch"),

    #path("comment", views.comment, name="comment"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    #path("<int:listing_id>", views.comment, name="comment")


]
