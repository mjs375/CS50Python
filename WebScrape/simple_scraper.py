"""
Python program takes a URL and opens the webpage, returning the complete HMTL as a string.
    Use Regex, BeautifulSoup, MechanicalSoup, &c. in later programs to extract data from the entire HTML string to just get the data you want.
Run the following code, with the website URL as an argument:
    $ python3 simple_scraper.py [url]
"""

from urllib.request import urlopen # tools for working with URLs: urlopen() can open a URL within a program
import sys
    # sys.argv : extracts argument vectors entered as command-line arguments
        # print("Name of script:", sys.argv[0])
        # print("Arguments of the script:", sys.argv[1:])
    # exit() : terminates Python program




# url = "http://olympus.realpython.org/profiles/aphrodite" # webpage URL to open
url = sys.argv[1] # url isn't hard-coded, enter as cmd-line argument
try:
    page = urlopen(url) # open the webpage
        # Page = an HTTPResponse object
        # print(page) # http.client.HTTPResponse object at 0x105fef820
except ValueError: # url fails to opened
    sys.exit("ERROR: unknown url. Correct usage: '$ python3 simple_scraper.py url'.")

html_bytes = page.read() # HTTPResponse object.read()'s method returns a sequence of html_bytes
html = html_bytes.decode("utf-8") # decode bytes to a string, using UTF-8

print(html) # Now you can print the HTML to see the webpage contents!

"""
Now that you have ALL THE HTML, you can extract data from it in a couple different ways with more complicated programs.
"""
