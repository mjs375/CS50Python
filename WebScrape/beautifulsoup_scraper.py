from bs4 import BeautifulSoup
    # install: $ python3 -m pip install beautifulsoup4
from urllib.request import urlopen
import time

    # 01: get the HTML in Python as a string
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url) # open the URL
html = page.read().decode("utf-8") # assigns HTML to a string
soup = BeautifulSoup(html, "html.parser") # creates a BeautifulSoup object, in variable 'soup'

    # 02: LOOK
# print(html) # prints entire HTML + raw content within
# print(soup.get_text().replace("\n","")) #remove the excess '\n's
# print(soup.get_text()) #prints only raw text, HTML tags removed

    # 03:
img_objects = soup.find_all("img") # return a list of all instances of a particular tag (not strings, but instances of a Tag object:)
# print(img_objects) # => [<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]
images = [image for image in img_objects] # list comprehension
#print(images) # images[0], images[1]
#print(images[0].name) #returns a string containing the HTMl tag type (here, 'img')

#print(soup.title) # <title>Profile: Dionysus</title>
#print(soup.title.string) # Profile: Dionysus

print(soup.find_all("img", src="/static/dionysus.jpg"))
