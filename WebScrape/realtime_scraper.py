"""
Python program that webscrapes dynamically: collects randomized dice-roll & timestamp, then reloads page and collects again.
    $ python3 realtime_scraper.py
"""
import mechanicalsoup
import time # time.sleep(sec)



browser = mechanicalsoup.Browser() # create headless web browser instance
rolls = dict() #store dice-roll/timestamp
for i in range(4): # x4 dice rolls total
    page = browser.get("http://olympus.realpython.org/dice") # open the webpage
    roll_tag = page.soup.select("#result")[0] # find element with id=result (BeautifulSoup object's .select() method).
    result = roll_tag.text
    timestamp_tag = page.soup.select("#time")[0] # find element with id=time
    timestamp = timestamp_tag.text # get timestamp text only
    print(f"The result of the {timestamp} dice roll is {result}.")
    rolls[timestamp] = result # add: dict[key] = value
    if i < 3: time.sleep(2) # pause 2 sec after each roll (not after last roll!)

print(rolls) # print the dictionary
