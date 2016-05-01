#import the modules
import json
import re
import string

#global variables
document="nayak_nandan_tweet_data.txt"
Clinton="Clinton"
Sanders="Sanders"
Cruz="Cruz"
Kasich="Kasich"
Trump="Trump"

hcIdx=0   #Index for all the presidential candidates in presidentList
bsIdx=2   #hc-Hillary Clinton, tc-Ted Cruz and so on...
tcIdx=4
jkIdx=6
dtIdx=7

presidentList=['hillary','clinton','bernie','sanders','ted','cruz','kasich','donald','trump']
presidentDict={
    Clinton:{},
    Sanders:{},
    Cruz:{},
    Kasich:{},
    Trump:{}
    }
candidateVotes={
    Clinton:0,
    Sanders:0,
    Cruz:0,
    Kasich:0,
    Trump:0
    }

commentShare={
    Clinton:0.0,
    Sanders:0.0,
    Cruz:0.0,
    Kasich:0.0,
    Trump:0.0
    }



#define all functions
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True

def fillPresDict(prez,loc):
    global presidentDict
    if loc not in presidentDict[prez]:
        presidentDict[prez][loc]=1
    else:
        presidentDict[prez][loc]+=1



#main function
if __name__=="__main__":
    txtfile=open(document,"r+")
    count=0
    for line in txtfile:
        if is_json(line):
            each_tweet=json.loads(line)
            user=each_tweet["user"]
            location=user["location"]
            if location!= None:
                text=each_tweet["text"]                 #Extract the text from tweet dictionary    
                text=re.sub(r'https[\w\d\s.\W]*'," ",text)   #Remove https..... string
                text=re.sub(r' [\d]* '," ",text)            #Remove strings that are only numbers
                text=re.sub(r'@[\w\d]*'," ",text)           #Remove @ followed by word/number
                text=re.sub(r'#[\w\d]*'," ",text)            #Remove Hashtags   
                text=re.sub(r'RT[@\w\d]*'," ",text)        #Remove RT.... words 
                text=text.encode('utf-8').translate(None,string.punctuation) #Remove punctuations
                text=text.lower()                       #Convert the string to lower
                text=text.split()
                location=location.split(",")
                location=location[0]
                location=location.lower()

                #print text
                for word in text:
                    if word == presidentList[hcIdx] or word == presidentList[hcIdx+1]:
                        fillPresDict(Clinton,location)
                        count+=1
                        #print text

                    elif word == presidentList[bsIdx] or word == presidentList[bsIdx+1]:
                        fillPresDict(Sanders,location)
                        count+=1
                        #print text

                    elif word == presidentList[tcIdx] or word == presidentList[tcIdx+1]:
                        fillPresDict(Cruz,location)
                        count+=1
                        #print text

                    elif word == presidentList[jkIdx]:
                        fillPresDict(Kasich,location)
                        count+=1
                        #print text

                    elif word == presidentList[dtIdx] or word == presidentList[dtIdx+1]:
                        fillPresDict(Trump,location)
                        count+=1
                        #print text


    print presidentDict
    print
    print "********************************************"
    print "Most Talked about US Presidential Candidates"
    print "********************************************"
    
    for eachPrez in presidentDict:
        votes=0        
        for eachLoc in presidentDict[eachPrez]:            
            votes+=presidentDict[eachPrez][eachLoc]
        candidateVotes[eachPrez]=votes
        if count ==0:
          voteShare=0.0
        else:
          voteShare=float(votes)/float(count)*100
        commentShare[eachPrez]=voteShare
    tempList=sorted(commentShare.items(),key=lambda(k,v):(-v,k))
    
    for prez in tempList:
       print "%s : %.2f%%"%(prez[0],prez[1])
        
     
                    
            
#close all files
    txtfile.close()
