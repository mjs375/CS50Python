import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    # Get start and end points [posts]
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

#Homemade API: type this into the browser
    # http://127.0.0.1:8000/posts?start=23&end=59

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })
