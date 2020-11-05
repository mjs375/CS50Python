from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #default route loads index function in views.py
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("emails", views.compose, name="compose"),
    path("emails/<int:email_id>", views.email, name="email"), #access a specific email, by email_id
    path("emails/<str:mailbox>", views.mailbox, name="mailbox"), #access inbox/sent/archive
]
