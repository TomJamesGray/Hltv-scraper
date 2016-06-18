#!/usr/bin/env python3
from lxml import html
import requests
import sys
import logging
def stripList(data):
    for i in range(0,len(data)):
        data[i] = str(data[i]).strip()

    return data
def main():
    logging.basicConfig(level=logging.DEBUG)

    #Get raw match page from hltv
    page = requests.get('http://www.hltv.org/matches/')
    logging.info("Code {} from hltv request".format(page.status_code))

    #Check status code - 200 is good
    if not page.status_code == 200:
        sys.exit(1)
    tree = html.fromstring(page.content)
    #Get the data from the page
    teamOne = stripList(tree.xpath("///div[@class='matchTeam1Cell']/a/text()"))
    teamTwo = stripList(tree.xpath("///div[@class='matchTeam2Cell']/a/text()"))
    print(teamOne)
    print(teamTwo)

if __name__ == "__main__":
    main()
