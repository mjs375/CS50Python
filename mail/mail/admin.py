from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Email # all model classes go here

# Register your models here.

"""
$ python3 manage.py createsuperuser
    Navigate to http://127.0.0.1:8000/admin to go to the native Django administrative page.
    Easily create, edit, and delete objects stored in the DB.
"""

#class ClassName(admin.ModelAdmin):
    #list_display = ("owner", "title", "desc", "startbid")


    # Register your models here to manipulate in the Admin interface:
# admin.site.register(class)
admin.site.register(User, UserAdmin)
admin.site.register(Email)
