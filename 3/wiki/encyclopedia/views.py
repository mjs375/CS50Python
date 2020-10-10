from django.shortcuts import render

from . import util #from this directory, get "util.py"
from markdown2 import Markdown #for styling wiki entries with Markdown
import random #for randint() #random.randint()
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms



#RENDERS INDEX HOMEPAGE, LISTS ENTRIES.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() #CONTEXT: all entries
    })



## Visit wiki/TITLE, renders the TITLE page (e.g. /wiki/HTML) from get_entry(title)
    #using get_entry() from encyc/util.py:
def entry(request, title): #input: 'title' string from URL path (wiki/"___")
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title), #get_entry uses the title to lookup #CONTEXT:
        "title":title
        # if entry == None:
            # return
    })


## GENERATES A RANDOM PAGE FOR "Random Page" link on sidebar:
def randomizer(request):
    if request.method == "GET":
        titles = util.list_entries() #obtain LIST of all entry TITLES
        random_num = random.randint(0, len(titles) - 1) #get a random number
        #zero-index* #random.randint(a,b) #a,b:range
        title = titles[random_num] #assign the entries[random_num as list-index]
        return entry(request, title) #calls on entry() now, submitting the randomized title to get the entire entry content

class NewEntryForm(forms.Form):
    new_entry = forms.CharField(label="Create a New Entry", widget=forms.Textarea)
    new_title = forms.CharField(label="Create Title", widget=forms.TextInput)
# # #
## Create a New Page: user can create a new wiki entry, enter Title & content(textarea)
def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {
            "form": NewEntryForm() #gives template access to variable 'form' that is a NewEntryForm object
        })
    else: #request.method == "POST" (user submits form)
        form = NewEntryForm(request.POST) #fill the form with submitted data
        if new_title not in util.list_entries(): #otherwise title is already taken (existing entry)

        #title_check = util.list_entries(new_title)


            if form.is_valid(): #check form is validation
                new_entry = form.cleaned_data["new_entry"] #get the new_entry
                new_title = form.cleaned_data["new_title"] #get the new_title
                util.save_entry(new_title, new_entry) #save the new entry (function from util.py)
                return entry(request, new_title)
        else: #form is NOT valid:
            return render(request, "encyclopedia/new.html", {
            "form": form #sends back existing form data to them to correct
            })









## Search box in sidebar should redirect to entered entry,
    # else partially match (Py->Python)






## Edit page: on each entry page the user should be able to click
 # an 'edit' link to edit the Markdown in a TEXTAREA (pre-populated with existing content)
