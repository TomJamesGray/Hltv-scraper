import sqlite3
import pytest
import os
from helpers import retrieveMatchUrls
dbFile = os.path.abspath("matches.db") 
@pytest.fixture
def insertTestData(request):
    global dbFile
    print(dbFile)
    if not os.path.isfile(dbFile):
        print("Db is not present")
        return False
    else:
        print("Db is present")
    
    conn = sqlite3.connect(dbFile)
    curs = conn.cursor()
    curs.execute("INSERT INTO matches (Team1,Team2,MatchUrl,MatchDate) \
        VALUES ('TeamOne','TeamTwo','AMatchUrl','TheMatchDate')")
    conn.commit()

    print("Set up")
    def tearDown():
        print("Removing test data from db")
        #Have to do this weirdly because by default sqlite doesn't
        #support a limit on DELETE
        curs.execute("DELETE FROM matches WHERE rowid=( \
                SELECT rowid FROM matches WHERE MatchUrl='AMatchUrl' AND MatchDate='TheMatchDate')")
        conn.commit()
        print("Test data removed")
        conn.close()
    request.addfinalizer(tearDown)
    return True

def testRetrieveMatchUrls(insertTestData):
    global dbFile
    urls = retrieveMatchUrls(dbFile)
    assert "AMatchUrl" in urls
