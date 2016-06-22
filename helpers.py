import sqlite3
#Strip whitespace and remove blak elements from list
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


#Retrieve all matchUrls from the specifieid db, returns them
#in a list containing strings
def retrieveMatchUrls(db):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    try:
        curs.execute("SELECT MatchURL FROM matches")
        matchUrls = curs.fetchall()
    except Exception as e:
        print(e)
    #Get the values out of the tuples and put them in a list of
    #just the URLs
    UrlList = []
    for elem in matchUrls:
        UrlList.append(elem[0])
    return UrlList
#Remove duplicates from the first arg that duplicate those in the 
#second arg. The 3rd arg is optional and removes elements with the same
#index that are going to be removed from the first arg
#All arguments should be provided as a list and the third arg should be
#a list of list(s)
#It will return a list of lists with the first arg as the first list in the
#list and the other optional lists (3rd arg) in the same order
def removeDuplicates(removeFromThisList,compareTo,removeByIndex=None):
    print(len(removeFromThisList))
    indexesToRemove = [x for x in range(0,len(removeFromThisList))
            if removeFromThisList[x] in compareTo]
    print(indexesToRemove)
    
    for i in sorted(indexesToRemove,reverse=True):
        del removeFromThisList[i]
        if isinstance(removeByIndex,list):
            for extraList in removeByIndex:
                del extraList[i]
    return [removeFromThisList,removeByIndex]
