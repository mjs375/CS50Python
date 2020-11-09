"""
Wikipedia Scraping: Pull all Linked Wiki Articles from Article.
    $ python3 wikipedia_scraper.py [url]
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
    # ^^ dealing with SSLCertVerificationError

def wikiscraping():

# # # 0. Check URL input:
    if sys.argv[2:]: # only 1 argument should be provided
        sys.exit("Too many arguments provided. Usage: $ python3 wikipedia_scraper.py [url]")
    try:
        sys.argv[1] # check if exists
        url = sys.argv[1]  # "https://en.wikipedia.org/wiki/Codewars"
    except: # if URL fails (or doesn't exist), ask for one:
        url = input("Please provide a valid URL: ")


# # # 1. Open the Page, Prepare Soup:
    try:
        page = urlopen(url) # open the webpage
        html = page.read().decode('utf-8') # converts to HTML, returns a string
        soup = BeautifulSoup(html, "html.parser") # creates a BeautifulSoup object
        #print(soup.title.string)
    except:
        sys.exit("URL provided failed to return response.")


# # # 2. Limit HTMl to div(id="bodyContent")
    content_soup = soup.find("div", {"id": "bodyContent"})
    print(content_soup)


# # # 3. Search out links, limit to Wiki Article links only: add to dict{}
    title_link = {}
    for link in content_soup.find_all("a"):
        if link.has_attr('href') and link.has_attr('title'):
            link_url = "https://en.wikipedia.org" + link['href']
            if ":" not in link['title']:  # only Wiki Articles, not Category pages ("Category:...") or ("Help:...")
                title_link[link['title']] = link_url # add to dict{}
    print(title_link)
    return title_link







# # # CALL THE FUNCTION:
wikiscraping()
# # #
