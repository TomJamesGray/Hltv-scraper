#!/usr/bin/env python3
from lxml import html
import requests
import sys
import logging
def main():
    logging.basicConfig(level=logging.DEBUG)

    #Get raw match page from hltv
    page = requests.get('http://www.hltv.org/matches/')
    logging.info("Code {} from hltv request".format(page.status_code))

    #Check status code - 200 is good
    if not page.status_code == 200:
        sys.exit(1)
    tree = html.fromstring(page.content)
    teamOne = tree.xpath("///div[@class='matchTeam1Cell']/a/text()")
    teamTwo = tree.xpath("///div[@class='matchTeam2Cell']/a/text()")

    print(teamOne)
    print(teamTwo)
if __name__ == "__main__":
    main()
