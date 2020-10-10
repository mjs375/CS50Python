from django.shortcuts import render
import datetime

# $ python3
    # [Opens up Python3 interpreter: lets you run Python code in the Terminal]

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
