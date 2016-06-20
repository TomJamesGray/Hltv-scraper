#!/usr/bin/env python3
from lxml import html
import requests
import sys
import logging
import sqlite3
baseURL = "http://www.hltv.org/"
def stripList(data):
    for i in range(0,len(data)):
        data[i] = str(data[i]).strip()
   
    #Remove blanks from list
    data = list(filter(None,data))
    return data

#Strip a string from all elements in a list
def stripFromList(data,toStrip):
    for i in range(0,len(data)):
        data[i] = data[i].strip(toStrip)

def insertMatchData(teamOne,teamTwo,db):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    if not len(teamOne) == len(teamTwo):
        raise ValueError("Amount of teams in matches aren't equal")
        sys.exit(1)

    for i in range(0,len(teamOne)):
        curs.execute("INSERT INTO matches ('Team1','Team2') VALUES (?,?)",(teamOne[i],teamTwo[i]))

    conn.commit()

def main():
    global baseURL
    logging.basicConfig(level=logging.DEBUG)

    #Get raw match page from hltv
    page = requests.get(baseURL + "matches/")
    logging.info("Code {} from hltv request".format(page.status_code))

    #Check status code - 200 is good
    if not page.status_code == 200:
        sys.exit(1)
    tree = html.fromstring(page.content)
    #Get the data from the page
    teamOne = stripList(tree.xpath("///div[@class='matchTeam1Cell']/a/text()"))
    teamTwo = stripList(tree.xpath("///div[@class='matchTeam2Cell']/a/child::text()"))
    #Get match url
    matchUrl = stripList(tree.xpath("///div[@class='matchActionCell']/a/@href"))
    print(matchUrl)
#    print("Length teamOne {} \nLengthTeamTwo {}".format(len(teamOne),len(teamTwo)))
    print("Inserting into db")
    insertMatchData(teamOne,teamTwo,"matches.db")
if __name__ == "__main__":
    main()
