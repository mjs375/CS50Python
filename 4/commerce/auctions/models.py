from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

""" ANYTIME YOU MAKE CHANGES TO MODELS.PY:
$ python3 manage.py makemigrations auctions
    [Make migrations for app]
$ python3 manage.py migrate
    [Apply migrations to your DB]
$ python3 manage.py runserver
    [Re-run the server]
"""









class User(AbstractUser):
    #AbstractUser is a MODEL that comes with Django
    #inherits from AbstractUser, already has fields for a username, email, password
    pass





class Listing(models.Model): #AUCTION LISTINGS
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_owner")
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    startbid = models.IntegerField()

    # image_url
    image = models.CharField(max_length=300, null=True) #null=True(image NOT required, can be left blank)
    #image = models.URLField #default max_length=200

    # STRING REP:
    #def __str__(self):
        #return f"{self. }...{self. }"


class Comment(models.Model): #COMMENTS ON AUCTION LISTINGS
    pass



class Bid(models.Model): #AUCTIONS BIDS
    # Many People can bid on Many Listings
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listing")
    bid = models.IntegerField()
    #bidder =




#
