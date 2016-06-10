#import all modules
import sys
import string
import re
import MapReduce
import matplotlib.pyplot as plt

#declare all global variables
mr = MapReduce.MapReduce()
scores = {}
sentiment={}
tweet_count=0
doc1="AFINN-111.txt"
doc2="nayak_nandan_tweet_data.txt"
doc3="results.txt"
presidentList=['hillary','clinton','bernie','sanders','ted','cruz','kasich','donald','trump']
clinton=["hillary","clinton"]
sanders=["bernie","sanders"]
cruz=["ted","cruz"]
kasich=["kasich"]
trump=["donald","trump"]
pos="pos"
neg="neg"
presidentDict={
    "Clinton":{pos:0,neg:0},
    "Sanders":{pos:0,neg:0},
    "Cruz":{pos:0,neg:0},
    "Kasich":{pos:0,neg:0},
    "Trump":{pos:0,neg:0}
    }
commentShare={
    "Clinton":0.0,
    "Sanders":0.0,
    "Cruz":0.0,
    "Kasich":0.0,
    "Trump":0.0
    }

#define functions
def fillCommentShare(myDict):
    count=0
    for eachPrez in myDict:
        count+=myDict[eachPrez][pos]
    for eachPrez in myDict:
        vote=float(myDict[eachPrez][pos])/float(count)*100
        vote=float("{0:.2f}".format(vote))
        commentShare[eachPrez]=vote
        

def fillDict(prezName,val):
    if val>=0:
        presidentDict[prezName][pos]+=1
    else:
        presidentDict[prezName][neg]+=1

def fillPrezDict(myList):
    value=myList[1][0]           
    if myList[1][1] in clinton:
        fillDict("Clinton",value)
    elif myList[1][1] in sanders:
        fillDict("Sanders",value)
    elif myList[1][1] in cruz:
        fillDict("Cruz",value)
    elif myList[1][1] in kasich:
        fillDict("Kasich",value)
    elif myList[1][1] in trump:
        fillDict("Trump",value)
                

def getPrezName(word):
    for i in range(len(presidentList)):
        if word == presidentList[i]:
            return presidentList[i]       
    

def checkTweet(tweet):
    for eachWord in tweet:
        if eachWord in presidentList:
            prezName = getPrezName(eachWord)
            return True,prezName
        else:
            continue
    return False, " "


def mapper(each_tweet):
    # Mapper code goes in here
    afinnfile = open(doc1)           # Make dictionary out of AFINN_111.txt file.
    for line in afinnfile:
        term, score  = line.split("\t")     # The file is tab-delimited. #\t means the tab character.
        scores[term] = int(score)           # Convert the score to an integer.
    text=each_tweet["text"]                 #Extract the text from tweet dictionary    
    text=re.sub(r'https[\w\d\s.\W]*'," ",text)   #Remove https..... string
    text=re.sub(r' [\d]* '," ",text)            #Remove strings that are only numbers
    text=re.sub(r'@[\w\d]*'," ",text)           #Remove @ followed by word/number
    text=re.sub(r'#[\w\d]*'," ",text)            #Remove Hashtags   
    text=re.sub(r'RT[@\w\d]*'," ",text)        #Remove RT.... words 
    text=text.encode('utf-8').translate(None,string.punctuation) #Remove punctuations
    text=text.lower()                       #Convert the string to lower
    text=text.split()                       #Convert the string into list of words
    #print text
    sentiment_score=0
    global tweet_count
    tweet_count+=1                          #Keep track of the tweet count
    flag,prezName = checkTweet(text)                   #Check for presidential candidates in tweet
    if flag==True:
        for word in text:
            if word in scores:
                sentiment_score+=scores[word]   #If the word in the tweet matches with the word in the AFINN.txt file, increment the sentiment score
        mr.emit_intermediate(tweet_count,[float(sentiment_score),prezName])

def reducer(key, list_of_values):
    # Reducer code goes in here
    resultList=[]
    resultList.append(key)
    resultList.append(list_of_values[0])
    fillPrezDict(resultList)
    mr.emit((key,list_of_values[0]))
    


#main function
if __name__ == '__main__':
    afinnfile = open(doc1)       # Make dictionary out of AFINN_111.txt file.
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. #\t means the tab character.
        scores[term] = int(score)  # Convert the score to an integer.
    tweet_data = open(doc2)
    mr.execute(tweet_data, mapper, reducer)
    
    fillCommentShare(presidentDict)
    
    tempList=sorted(commentShare.items(),key=lambda(k,v):(-v,k))


    sizes=[]
    labels=[]
    negt=[]
    for tup in tempList:
        labels.append(tup[0])
        sizes.append(tup[1])
    colors=["pink","magenta","yellow","orange","green"]

    plt.pie(sizes,labels=labels,autopct="%.2f%%",startangle=-45,colors=colors)
    plt.axis("equal")
    plt.title("US Presidential Election Forecast (Vote Share based on positive comments)")
    plt.show()

    


    







    
    

