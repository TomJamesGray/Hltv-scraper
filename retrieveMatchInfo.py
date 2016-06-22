import requests
import logging
import sys
import time
from helpers import stripList
from lxml import html
#Retrieve the date and time for the match from the 
#given url and return it in form YYYYMMDD HH:MM
def getGameTime(url):
    page = requests.get(url)
    logging.info("Code {} from request".format(page.status_code))
    if not page.status_code == 200:
        sys.exit(1)
    tree = html.fromstring(page.content)
    #Remove the st,rd... at the end of the date and the of to make it easier to read
    dateAndTime = tree.xpath("///div[@class='centerFade']/div[1]/div[2]/span[1]/text()")[0].strip().replace(
            "of ","").replace("st","").replace("th","").replace("rd","").replace("nd","")
    dateAndTime = dateAndTime + " " + tree.xpath("///div[@class='centerFade']/div[1]/div[2]/span[2]/text()")[0].strip()
    #Get time object from date retrieved
    dateObj = time.strptime(dateAndTime,"%d %B %Y %H:%M")
    return time.strftime("%Y%m%d %H:%M",dateObj)
