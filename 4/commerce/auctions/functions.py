from .models import User, Listing, Bid, Comment #import Class-es from models.py:



## Returns the highest bid for any listed item:
def maxxer(listing_id):
    getstartbid = Listing.objects.filter(pk=listing_id).values("startbid")#gets list of x1 DICT [{"startbid": "30"}], by filtering model Listing for this particular listing_id passed in from the URL_page...
    startbid = getstartbid[0]["startbid"] # the actual startbid value, "30"
    bids_list = list(Bid.objects.filter(bid_listing=listing_id).values("bid")) # Returns list of DICTS
        #TEST: print(f"Startbid:{startbid}, bids:{bids_list}, CHECK") #TEST
    newbidslist = [] #empty list to stick values in
    if bids_list: # check if bids have been made at all (besides base startbid):
        for item in bids_list: #iterate thru each DICT in the LIST:
            for key, value in item.items(): #append VALUE to LIST from particular DICT:
                if key == "bid":
                    newbidslist.append(value)
                    #TEST: print(f"Startbid:{startbid}, bids:{newbidslist}, CHECK") #TEST
    # CHECK FOR THE MAX BID
    if newbidslist:
        max_bid = int(max(newbidslist)) #obtain the max bid from the list of made-bids
    else:
        max_bid = int(startbid) -1 #no one has bid yet, start with the original startbid
    return max_bid
###



#
