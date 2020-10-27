from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

from django.db.models import Max #delete if unnecessary


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
    watchlist = models.ManyToManyField("Listing", blank=True, related_name="watchlist") #contains Listing objects
    #IF* User & Listing reference[d] each other, and User comes first, it must call the name of Listing ('Listing'), rather than the model itself.
    #blank=True [a User is allowed to have no watchlist items]



class Bid(models.Model): #AUCTIONS BIDS
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder", null=True)
    bid_listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bids", null=True)
    bid = models.PositiveIntegerField(null=True)


class Listing(models.Model): #AUCTION LISTINGS
    # id [auto-generated]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_owner")
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    startbid = models.IntegerField()
    image = models.CharField(max_length=300, null=True, blank=True) #null=True(image NOT required, can be left blank)
    #
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", blank=True, default=None, null=True)
    #
    #category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="listing_cat", null=True)
    #
    LIST_CATS = [
        ('BOOKS', 'Books'),
        ('BROOMS', 'Brooms'),
        ('DARK MAGIC', 'Dark Magic'),
        ('ENCHANTED ITEMS', 'Enchanted Items'),
        ('MISC.', 'Misc.'),
        ('POTIONS', 'Potions'),
        ('TOYS', 'Toys'),
        ('WANDS', 'Wands'),
    ]
    #
    category = models.CharField(choices=LIST_CATS, blank=True, null=True, max_length=200)
    #
    #
    bigbid = models.IntegerField(null=True)
    #



# # # # #


class Comment(models.Model): #COMMENTS ON AUCTION LISTINGS
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True) #commenter
    #
    comment_text = models.CharField(max_length=1000, null=True) #comment
    #
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", null=True)
    # datetime = models.DateTimeField(default=timezone.now)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
