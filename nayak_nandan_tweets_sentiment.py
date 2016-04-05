import sys
import string
import re
import MapReduce

mr = MapReduce.MapReduce()
scores = {}
sentiment={}
tweet_count=0


def mapper(each_tweet):
    # Mapper code goes in here
    afinnfile = open(sys.argv[1])           # Make dictionary out of AFINN_111.txt file.
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
    sentiment_score=0
    global tweet_count
    tweet_count+=1                          #Keep track of the tweet count
    for word in text:
        if word in scores:
            sentiment_score+=scores[word]   #If the word in the tweet matches with the word in the AFINN.txt file, increment the sentiment score
    mr.emit_intermediate(tweet_count,float(sentiment_score))

def reducer(key, list_of_values):
    # Reducer code goes in here
    mr.emit((key,list_of_values[0]))


if __name__ == '__main__':
    afinnfile = open(sys.argv[1])       # Make dictionary out of AFINN_111.txt file.
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. #\t means the tab character.
        scores[term] = int(score)  # Convert the score to an integer.
    tweet_data = open(sys.argv[2])
    mr.execute(tweet_data, mapper, reducer)


