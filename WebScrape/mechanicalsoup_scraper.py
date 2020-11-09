"""
A Python webscraper using MechanicalSoup to 1. login in to a website using a form, and 2. scrape some link data.
    $ python3 mechanicalsoup_scraper.py [url]
"""
import sys #sys.exit
import mechanicalsoup # ($ python3 -m pip install MechanicalSoup)
import getpass # hides password when called for (in terminal)
import time




# # # 1. PREPARE A BROWSER
# # # # # # # # # # # # # #
browser = mechanicalsoup.Browser() # create a headless web browser instance


# # # 2. ATTEMPT TO OPEN WEBPAGE WITH [URL] PROVIDED:
if sys.argv[2:]: # Only 1 additional argument needed: [url]
    sys.exit("Too many arguments provided. Correct usage: '$ python3 mechanicalsoup_scraper.py url'")
try:
    # url = "http://olympus.realpython.org/login" # hard-coded URL
    url = sys.argv[1] # url isn't hard-coded, enter as cmd-line argument
    login_page = browser.get(url) # request webpage from Internet; page stores response
except IndexError: # URL not provided
    sys.exit("Correct usage: '$ python3 mechanicalsoup_scraper.py url'")
except ValueError: # url fails to opened
    sys.exit("ERROR: unknown url.")

login_html = login_page.soup # HTML of webpage (page's .soup attribute)
    # print(type(page.soup)) # .soup attribute represents a BeautifulSoup object: <class 'bs4.BeautifulSoup'>
    # print(login_page.title.string)
    # print(login_page.url)


# # # 3. SUBMIT THE LOGIN FORM
# # # # # # # # # # # # # # # #
username = input("Username: ") # prompt for credentials
password = getpass.getpass("Password: ") # hides pwd as you type
    # u:"zeus", p:"ThunderDude"

form = login_html.select("form")[0] #
form.select("input")[0]["value"] = username # fill-in username
form.select("input")[1]["value"] = password # fill-in password

profiles_page = browser.submit(form, login_page.url) # submit form
    # print(profiles_page.url)


# # # 4. SCRAPE THE DATA
# # # # # # # # # # # # #
links = profiles_page.soup.select("a") # select all <a> elements
base_url = "http://olympus.realpython.org" # for completing relative links
for link in links: # iterate the links
    address = base_url + link["href"] # access the href attribute of each link
    text = link.text
    print(f"{text}: {address}")
    time.sleep(0.5)




#
