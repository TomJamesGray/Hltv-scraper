#!/usr/bin/env python3
from lxml import html
from helpers import stripList,stripFromList
import retrieveMatchInfo
import requests
import sys
import logging
import sqlite3
baseURL = "http://www.hltv.org"
#Insert data to the db
def insertMatchData(teamOne,teamTwo,matchUrl,matchDate,db):
    global baseURL
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    if not len(teamOne) == len(teamTwo):
        raise ValueError("Amount of teams in matches aren't equal")
        sys.exit(1)

    for i in range(0,len(teamOne)):
        try:
            curs.execute("INSERT INTO matches ('Team1','Team2','MatchUrl','MatchDate') VALUES (?,?,?,?)",
                (teamOne[i],teamTwo[i],matchUrl[i],matchDate[i]))
        except sqlite3.IntegrityError:
            logging.info("Duplicate match url {}".format(matchUrl[i]))
            logging.info("Skipping match")
            continue
    conn.commit()
def main():
    global baseURL
    logging.basicConfig(level=logging.DEBUG)

    #Get raw match page from hltv
    page = requests.get(baseURL + "/matches/")
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
    matchDate = []
    for i in range(0,len(matchUrl)):
        #Prepend the baseUrl to the match URL
        matchUrl[i] = baseURL + matchUrl[i]
        #use the matchUrl to retrieve the matchInfo
        matchDate.append(retrieveMatchInfo.getGameInfo(matchUrl[i]))
    insertMatchData(teamOne,teamTwo,matchUrl,matchDate,"matches.db")
if __name__ == "__main__":
    main()
