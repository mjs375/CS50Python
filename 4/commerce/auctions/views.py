from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Max

from .models import User, Listing, Bid, Comment #Category #import Class-es from models.py:
from .functions import maxxer #import f(x) to find highest bid


# message=None
def index(request, message=None):# 'message=None' makes {{message}} an optional parameter.
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(), #pull all listing objects and make accessible to index.html
        #
        "bids": Bid.objects.all()
        #
    })

def index2(request, message=None):
    return render(request, "auctions/index2.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST": #form submitted w/ credentials

        # Attempt to sign user in
        username = request.POST["username"] #get username from form
        password = request.POST["password"] # ditto
        user = authenticate(request, username=username, password=password) #check if valid user

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else: #bring user to the login form page:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



# DISPLAY INDIVIDUAL LISTING:
def listing(request, listing_id, message=None, max_bid=None): #
    listing = Listing.objects.get(pk=listing_id)
    max_bid = maxxer(listing_id) #call function to get highest bid yet

    if request.user.is_authenticated:
        watchlist = request.user.watchlist.all()
    else:
        watchlist = None #No user is logged in, so just feed an empty watchlist that nothing will be done with later
    return render(request, "auctions/listing.html", {
        "listing": listing, #object
        "watchlist": watchlist, #watchlist.html can access "watchlist" (also an object)
        "commentform": CommentForm(initial={'comment_author': request.user, 'comment_listing': listing_id}),
        "bidform": BidForm(initial={"bidder": request.user, "bid_listing": listing_id}),
        "message": message,
        "max_bid": max_bid
    })



"""
https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
^^^ Django Documentation for ModelForms
"""
# # #
class NewListingForm(forms.ModelForm): #creating a ModelForm subclass
    class Meta: #configures the model to work from
        model = Listing
        # fields = '__all__' #pulls all fields from the model to use
        # exclude = ['owner'] #excludes a particular field from the model (while including all others)

        fields = ['title', 'desc', 'startbid','owner', 'image', 'category'] #list of form fields, pulled from model 'Listing'

        labels = { # DICT
            'title': 'Title',
            'desc': 'Description of Item',
            'startbid': 'Starting Bid',
            'owner': 'Owner',
            'image': 'Item Image URL',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(), #this is actually the default
            'desc': forms.Textarea(),
            'startbid': forms.NumberInput(),
            'owner': forms.HiddenInput(), #because Listing poster shouldn't be able to 'choose owner', owner must always be them.
            'winner': forms.HiddenInput(),
            #'category': #default widget is select with choices dropdown
        }
#
# #
# # #
# #
#
@login_required
# CREATE A NEW LISTING:
def new(request):
    if request.method == "GET": # give the user
        return render(request, "auctions/new.html", {
            "form": NewListingForm(initial={'owner': request.user}) # creates an empty NewListingForm to display. Owner should automatically be set to 'request.user' and form should not allow that to be changed!
        })
    else: #POST:
        form = NewListingForm(request.POST) #create form instance from POST data
        #
        #
        if form.is_valid():
            form.save() #save a new Listing object from the form's data
            return index(request)
        else:
            return index(request, message="Listing posting failed.")








# GENERATES LIST OF 'WATCHED' LISTINGS ON ".../WATCHLIST"
@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all() #watchlist.html can access "watchlist"
    })

# ADDS LISTING FROM LISTING.html TO USER'S WATCHLIST
@login_required #if the user isn't logged in, it redirects; else...
def add_watch(request, listing_id): # User presses 'Watch' button:
    watch_listing = Listing.objects.get(pk=listing_id) #access the listing
    request.user.watchlist.add(watch_listing) # Add 'watch_listing' to the watchlist of the user that made the request
    return watchlist(request)

# REMOVES LISTING FROM LISTING.html TO USER'S WATCHLIST
@login_required
def remove_watch(request, listing_id):
    watch_listing = Listing.objects.get(pk=listing_id) #access the listing
    request.user.watchlist.remove(watch_listing) # Remove 'watch_listing' to the watchlist of the user that made the request
    return listing(request, listing_id)


class CommentForm(forms.ModelForm):
    class Meta: #configures the model to work from (Comment):
        model = Comment
        fields = [
        "comment_author",
        "comment_text",
        "comment_listing"
        ] #pull all fields from class Comment
        labels = {
            "comment_text": "Comment"
        }
        widgets = {
            "comment_author": forms.HiddenInput(),
            "comment_text": forms.Textarea(),
            "comment_listing": forms.HiddenInput()
        }
#
# #
# # #
# #
# ADD A COMMENT TO A PARTICULAR ACTIVE LISTING
@login_required
def comment(request, listing_id):
    if request.method == "GET":
        return listing(request, {
            "commentform": CommentForm(initial={"comment_author": request.user, "comment_listing": listing_id})
        })
    else: # form submitted:
        commentform = CommentForm(request.POST) #create instance of form from POST data
        if commentform.is_valid(): #validate the form...
            commentform.save() #save a new Comment Object from the form's data
            #return HttpResponseRedirect(reverse("index")) #COMMENT SUCCESSFULLY SUBMITTED
            return listing(request, listing_id)
        else: #form somehow fails to validate...:
            return index(request, message="The comment failed to submit.")



class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        labels = {
            "bidder": "Bidder",
            "bid": "Bid",
            "bid_listing": "Listing"
        }
        widgets = {
            "bidder": forms.HiddenInput(),
            "bid": forms.NumberInput(),
            "bid_listing": forms.HiddenInput(),
            'winner': forms.HiddenInput()
        }
#
# #
# # #
# #
#
def bid(request, listing_id):
    # # # # # # #
    max_bid = maxxer(listing_id) #call maxbid function
    # # # # # # # #
    # #
    if request.method == "GET": #GIVE USER A BLANK BID FORM
        return listing(request, {
            "bidform": BidForm(initial={"bidder": request.user, "bid_listing": listing_id})
        })
    # # #
    # # #
    else: #FORM submitted w/ data via POST:
        bidform = BidForm(request.POST) #populate form with POST data via request.
        ## BIDDING CHECKS:
        if bidform.is_valid(): #validate the form...
            #CHECK BID IS HIGH ENOUGH:
            mybid = int(request.POST.get('bid')) # what the user tried to field('bid')
            if mybid > max_bid:
                bidform.save() #save the bid to the DB
                message = "Bid successfully placed!"
                #
                max_bid = maxxer(listing_id) #call maxbid function #Update max_bid AFTER the latest bid was (just) placed
                max_bid = int(max_bid) #for html purposes
                #
                #
                # # Update the listing's new max_bid in the Listing model
                a = Listing.objects.get(pk=listing_id)
                a.bigbid = max_bid #updates the 'bigbid' field of Listing (saved as variable 'a'), sets it equal to max_bid
                a.save() #
                #
            else: # user's bid wasN'T the highest yet (or equal to the startbid)
                message = "Bid amount too small."

            #
            #
            return listing(request, listing_id, message=message, max_bid=max_bid)
        else: #form otherwise doesn't validate...
            return HttpResponseRedirect(reverse("index"))



def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user == listing.owner:
        # ADD CHECK TO SEE IF ANYONE ACTUALLY BID FOR ITEM AND A WINNER CAN BE DECLARED
        listing.active = False #owner closes the auction/listing status is inactivated
        # # #
        getbigbid = Bid.objects.filter(bid_listing=listing_id).aggregate(Max('bid'))
        bigbid = getbigbid['bid__max']
        getwinner = Bid.objects.filter(bid_listing=listing_id, bid=bigbid).values("bidder")
        try: # Have any bids been made (can a winner be declared?)
            winner = getwinner[0]['bidder'] #get dict value
            listing.winner = User.objects.get(pk=winner)
        except: # Auction is closed but no one actually bid:
            pass
        listing.save() #actually save the winner
        message = None
    else: #non-owner somehow accesses the page:
        message = "You cannot close another person's auction listing."
    return index(request)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def cats(request): #displays list of all categories
    categories = Listing.objects.order_by("category").values_list("category", flat=True).distinct()
    #categories = Category.objects.filter(active=True).order_by("cat").values_list("cat", flat=True).distinct()
    return render (request, "auctions/cat.html", {
        "categories": categories
    })


def cat(request, cat): #displays list of all listings per category [receives request and specific 'cat']
    catitems = Listing.objects.filter(category=cat)
    return render(request, "auctions/cat.html", {
        "category": cat,
        "catitems": catitems
        #"listings": Listing.objects.filter(category=cat).filter(active=True), #must use integer ID
#right cat is from def (cat)

    })




#
