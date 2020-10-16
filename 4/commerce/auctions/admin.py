from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Listing, Bid, Comment
    #all model classes go here



"""
Navigate to http://127.0.0.1:8000/admin to go to the native Django administrative page.
Easily create, edit, and delete objects stored in the DB.
"""

"""
# Configuration customization:
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
"""



# Register your models here.
    # admin.site.register(class)
admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)




#
