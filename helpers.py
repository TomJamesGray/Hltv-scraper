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

