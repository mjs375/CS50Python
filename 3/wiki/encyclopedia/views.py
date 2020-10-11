from django.shortcuts import render
from . import util #from this directory, get "util.py"
import random #for randint() #random.randint()
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages #for Error message

from markdown2 import Markdown #for styling wiki entries with Markdown
marker = Markdown()
# marker.convert("string") # usage: marker.convert(TARGET) [target must be a string]




#RENDERS INDEX HOMEPAGE, LISTS ENTRIES.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() #CONTEXT: all entries
    })



## Visit wiki/TITLE, renders the TITLE page (e.g. /wiki/HTML) from get_entry(title)
    #using get_entry() from encyc/util.py:
def entry(request, title): #input: 'title' string from URL path (wiki/"___")
    if title.lower() in [item.lower() for item in util.list_entries()]:
        return render(request, "encyclopedia/entry.html", { #CONTEXT:
            "entry": marker.convert(util.get_entry(title)), #get_entry uses the title to lookup,
            "title":title
        })
    else: #
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title),
            "title":title
        })


    #else: #title NOT IN list_entries()
        #return bad_entry(request, title)

## When user attempts to go to "/falsetitle":
#def bad_entry(request, falsetitle):
#    messages.error(request, "Page does not exist.")
#    return render (request, "encyclopedia/index.html", {
#        "entries": util.list_entries(),
#        "falsetitle": falsetitle
#    })



## GENERATES A RANDOM PAGE FOR "Random Page" link on sidebar:
def randomizer(request):
    if request.method == "GET":
        titles = util.list_entries() #obtain LIST of all entry TITLES
        random_num = random.randint(0, len(titles) - 1) #get a random number
        #zero-index* #random.randint(a,b) #a,b:range
        title = titles[random_num] #assign the entries[random_num as list-index]
        return entry(request, title) #calls on entry() now, submitting the randomized title to get the entire entry content






class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="Create Title", widget=forms.TextInput)
    new_entry = forms.CharField(label="Create a New Entry", widget=forms.Textarea)
# # #
## Create a New Page: user can create a new wiki entry, enter Title & content(textarea)
def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {
            "form": NewEntryForm() #gives template access to variable 'form' that is a NewEntryForm object
        })
    else: #request.method == "POST" (user submits form)
        form = NewEntryForm(request.POST) #fill the form with submitted data

        if form.is_valid(): #check form is validation
            new_title = form.cleaned_data["new_title"] #get the new_title
            new_entry = form.cleaned_data["new_entry"] #get the new_entry
        if util.get_entry(new_title) is None: #title does not already exist
            util.save_entry(new_title, new_entry) #save the new entry (function from util.py)
            return entry(request, new_title)
        elif util.get_entry(new_title) is not None: #title is already taken, return ErrorMessage:
            #https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html
            messages.error(request, "Title already taken.")
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
        else: #form is NOT valid, need to correct...
            return render(request, "encyclopedia/new.html", {
            "form": form #sends back existing form data to them to correct
            })




class EditEntryForm(forms.Form):
    editentry = forms.CharField(label="Edit Entry Content", widget=forms.Textarea)
# # #
# EDIT AN EXISTING ENTRY'S CONTENT:
def edit(request, title): #'title' is from url string 'wiki/____'
    if request.method == "GET":
        initial = {"editentry": util.get_entry(title)} # for re-populating field with old content...
        return render(request, "encyclopedia/edit.html", { # CONTEXT PASSED TO EDIT.HTML PAGE
            "entry": util.get_entry(title),
            "title":title,
            "form":EditEntryForm(initial=initial) # sets value of Textarea as previous content
        })

    else: # POST:
        form = EditEntryForm(request.POST)
        if form.is_valid():
            editentry = form.cleaned_data["editentry"]
            util.save_entry(title, editentry)
            return entry(request, title) #go back to entry page


## SEARCH:
"""
$ git branch
[new]
$ git checkout new
    (...finish search function...)
$ git commit -am "Finished search function"
$ git push
    (Now new'branch is saved:)
$ git checkout master
$ git merge new

$ python3 manage.py runserver

"""


## This matcher() checks for a matching substring (He - Hello)
def matcher(en_try, q):
    word = en_try
    for i in range(len(q)):
        if q[i] != word[i]:
            return # exit function, not a partial match!
    return word


#
def search(request):
    q = request.GET.get('q') # Obtain 'q' value from search form
    q = q.lower()
    new = util.list_entries() # Obtain LIST of entry titleS
    new = [item.lower() for item in new] # Lower-case the titleS
    #
    if q in new: #check if search term exactly matches an Entry in the returned LIST
        return entry(request, q) # if so, call on entry form, submit 'q' for 'title'
    if q == "": # if search bar is empty:
        return index(request) # Return the homepage
    #
    else: # Possible inexact match...
        matches = [] # empty list to store possible partial matches
        for title in new:
            if q in title:
                matches.append(title)
        return render(request, "encyclopedia/search.html", {
            "matches": matches,
            "q": q
        })


#        for en_try in new: # entry by entry, in list[] new
#            match = matcher(en_try, q)
#            if match != None:
#                matches_list.append(match)



#        return render(request, "encyclopedia/search.html", {
#            "entries": matches_list,
#            "q": q
#        })
# # # # #
