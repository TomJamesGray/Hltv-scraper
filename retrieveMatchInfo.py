import requests
import logging
import sys
from main import stripList
from lxml import html
#Retrieve the date and time for the match from the 
#given url and return it in form YYYYMMDD HH:MM
def getGameInfo(url):
    page = requests.get(url)
    logging.info("Code {} from request".format(page.status_code))
    if not page.status_code == 200:
        sys.exit(1)
    tree = html.fromstring(page.content)
    date = tree.xpath("///div[@class='centerFade']/div[1]/div[2]/span[1]/text()")
    print(date)

getGameInfo("http://www.hltv.org/match/2303150-natus-vincere-echo-fox-eleague-season-1")
