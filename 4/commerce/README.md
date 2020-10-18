# COMMERCE: PROJECT 2
#### *Matthew James Spitzer, October 15, 2020*




## **Project Checklist:**
- [x] **Create 'Listing' model**
- [ ] **Create 'Bid' model**
- [x] **Create 'Comment' model**
- [x] **Django Admin Interface**: *set up a Django Admin Interface to view, add, edit, or delete any comments, bids, or listings on the site.*
- [x] **Create Listing**: *Implement a 'Create a New Listing' page. Specify: title, description, starting bid, and (optionally) an image URL and/or category.*
- [x] **Active Listings Page**: *web homepage should let users view all currently active auction listings. For each one, display the title, description, current price, and photo.*
- [x] **Listing Page**: *clicking on an individual listing should take users to a specific page.*
    - [x] **Add to Watchlist**: *if a user is signed in, the user should be able to add the item to their Watchlist. If already added, they should instead have the option to remove it.*
    - [ ] **Bid on Item**: *if signed in, user should be able to bid on the item. Bid must be at least as large as the starting bid, or greater than any other bids. Create an error message for when this isn't the case.*
    - [ ] **Close Item Auction**: *if the user who created the item is signed in, they should be able to close the auction. Make the highest bidder the winner, and make the listing no longer active.*
    - [x] **Add Comments**: *signed in users should be able to add comments to the listing page. Display all comments made on the listing.*
    - [ ] **Closed Listing Page**: *if signed in on a closed listing page, it should say if the user has won that auction.*
- [x] **Watchlist Page**: *signed-in users should be able to visit a Watchlist page, which should display all listings that a user currently has added to their watchlist. Each item should be clickably-linked to the listing itself.*
- [ ] **Categories**: *users should be able to visit a page that displays a list of all listing categories. Clicking on any category should bring the user to a page that displays all the active listings in that category.*


### TERMINAL COMMANDS:
- *[$ django-admin startproject airline]*
- *[$ python3 manage.py startapp flights]*
- $ cd commerce
    - $ python3 manage.py makemigrations auctions [*Make migrations for app*]
    - $ python3 manage.py migrate [*Apply migrations to your DB*]
- $ python3 manage.py runserver [*Run server, copy & paste URL from terminal into browser to view website*]
    - *http://127.0.0.1:8000/*
    – *.../admin*
- Create an administrative User:
    - $ python3 manage.py createsuperuser
    - admin / H*!
#### GIT:
1. $ cd [directory]
2. $ git add . / $ git add <filename>
3. $ git commit -m "message"
    - $ git commit -am "messsage"
4. $ git push

[ ] $ submit50 web50/projects/2020/x/commerce
