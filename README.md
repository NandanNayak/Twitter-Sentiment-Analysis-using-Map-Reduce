<h1 align="center">US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap</h1>
<ol>
<li> Access the Twitter Application Programming Interface (API) using python</li>
<li>Estimate the public's perception (the sentiment) of the tweet’s</li> 
<li>Calculate the TF-DF (term frequency-document frequency) of terms in a tweet</li> 
<li>Derive the location of tweets</li>
<li>Plot the tweet locations against each Presidential candidate using ArcMap</li>  
</ol>

<strong>Input file</strong>

All the python files need the below text file as input data which is about 200 MB.

<a href="https://drive.google.com/folderview?id=0BxdLbeUsfPFvS1ZBMDh1OFU0bzA&usp=sharing">nayak_nandan_tweet_data.txt </a>

<strong>Project Report and Results</strong>

The Project report contains the results from Twitter Sentiment Analysis and also the locations mapped onto ArcMap from where the tweets were made about a US Presidential candidates.

<a href="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/Project_Report_And_Results.pdf">Project Report and Results</a>

<h3>Get Twitter Data</h3>
<ol>
<li>The twitterstream.py file is used to get live streaming twitter data</li>
<li>To access the live stream, the oauth2 library is used to properly authenticate</li> 
<li>Create a twitter account if you do not already have one. Respond to the resulting email from Twitter to confirm your Twitter Account</li>
<li>Go to https://dev.twitter.com/apps and log in with your twitter credentials</li>
<li>Click "Create New App”</li>
<li>Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use</li>
<li>On the next page, click the “Keys & Access Tokens” tab along the top, then scroll all the way down until you see the section "Your Access Token"</li>
<li>Click the button "Create My Access Token". You can Read more about Oauth authorization <a href="https://pypi.python.org/pypi/oauth2/">here</a></li>
<li>You will now copy four values into twitterstream.py</li>
<li>"API Key (Consumer Key)"</li>
<li>"API secret (Consumer Secret)"</li>
<li>"Access token"</li>
<li>"Access token secret"</li>
<li>Open twitterstream.py and you will see the code like below. Replace the corresponding values in the code</li>
<ul>
<li>api_key = "(Enter api key)"</li>
<li>api_secret = "(Enter api secret)"</li>
<li>access_token_key = "(Enter your access token key here)"</li>
<li>access_token_secret = "(Enter your access token secret here)”</li>
</ol>
<li>Run the following and make sure you see data flowing and that no errors occur</li></ol>
<strong><em>python twitterstream.py > nayak_nandan_tweet_data.txt</em></strong>
This command pipes the output to a file. Stop the program with Ctrl-C once the required amount of data is accumulated.

<h3>Python MapReduce Framework and Execution</h3>
A python library called MapReduce.py that implements the MapReduce programming model is used. The framework faithfully implements the MapReduce programming model, but it executes entirely on a single machine - it does not involve parallel computation.


<h3>Derive Tweet Sentiment Score</h3>
<ul>
<li> For this part, the MapReduce.py is used as framework and tweets_sentiment.py as a base for the script</li>
<li>Executing the code for the problem</li>
<strong><em>python nayak_nandan_tweets_sentiment.py</em></strong>

<p>The above file reads two files:
<li><em>AFINN-111.txt</em>: AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a tab separated sentiment score. </li>
<li>nayak_nandan_tweet_data.txt: The tweet data file created earlier</li></ul></p>

<strong>Sample Output</strong>
<a href="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/nayak_nandan_output_sentiment_scores.txt">nayak_nandan_output_sentiment_scores.txt</a>

<p><strong>Visualization</strong></p>
<img src="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/ElectionPrediction.png" align="center"/>

<h3> TF-DF of each term (term frequency – document frequency)</h3>

For this part, the MapReduce.py is used as framework and tweets_tfdf.py as a base for the script.
<ul>
<li>Executing the code for the problem:
<strong><em>python nayak_nandan_tweets_tfdf.py</em></strong>
<li>The above python file reads one file</li>
<li>nayak_nandan_tweet_data.txt: The tweet data file created earlier</li>
</ul>
<strong>Sample Output:</strong>
<a href="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/nayak_nandan_output_tfdf.txt">nayak_nandan_output_tfdf.txt</a>

<h3> Derive location of each tweet</h3>
</ul>
<li>Executing the code for the problem
python nayak_nandan_tweets_location.py 
<li>The above python file reads one file</li>
<li>nayak_nandan_tweet_data.txt: The tweet data file created earlier</li>
</ul>

<strong>Sample Output : </strong>
<a href="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/nayak_nandan_output_location.txt">nayak_nandan_output_location.txt</a>



<h3>Algorithm:</h3>
<h3>Derive Tweet Sentiment Score</h3>
<strong>Mapper</strong>
<ul>
<li>The input is a python dictionary containing the tweets data: each_tweet</li>
<li>Extract the ‘text’ from this tweet which is now stored in a dictionary. You can also read the Twitter documentation (https://dev.twitter.com/docs/platform-objects/tweets) to understand what information each tweet contains and how to access it, but it's not too difficult to deducethe structure by direct inspection</li>
<li>Now that the ‘text’ for each tweet is available, it is used to calculate the sentiment score of each tweet. For that you have to lookup each term of the tweet in the AFINN-111.txt dictionary and add up their respective sentiment scores</li>
<li>All the terms in AFINN-111.txt are lower case. So, use the string.lower() function to convert your tweet to all lower case for this problem</li>
<li>To encode the tweet string in utf-8 and remove ASCII punctuation, import the string library and use the following code:
newstring = mystring.encode('utf-8').translate(None, string.punctuation)</li>
<li>Some tweets contain URL’s (eg: https:\/\/t.co\/8wl9wrT), hashtags(starting with #,@) and prefix like “RT @ManUtd:”, which should be ignored while calculating the sentiment score. For this purpose python’s  regular expression library(import re) is used . Also the extra terms found in the tweets but not in AFINN-111.txt are given a sentiment score of 0</li>
</ul>
<strong>Reducer</strong>
<ul>
<li>The script should print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score corresponds to the first tweet, the second score corresponds to the second tweet, and so on. A sample output for reference is given below:
<p>[1, 2.0] # Sentiment score of tweet1 is 2</p>
<p>[2, 0] # Sentiment score of tweet2 is 0</p></li>
</ul>


<h3>TF-DF of each term(term frequency – document frequency)</h3>
<strong>Mapper</strong>
<ul>
<li>The input is a python dictionary containing the tweets data: each_tweet</li>
<li>Extract the ‘text’ from this tweet which is now stored in a dictionary. You can also read the Twitter documentation (https://dev.twitter.com/docs/platform-objects/tweets) to understand what information each tweet contains and how to access it, but it's not too difficult to deducethe structure by direct inspection</li>
<li>Now that the ‘text’ for each tweet is available, it is used to calculate the term frequency(tf) of each term of each tweet</li>
<li>Convert the string to lower case before calculating the tf. Also encode the string in utf-8 and remove ASCII punctuation by using:
<p><em>newstring = mystring.encode('utf-8').translate(None, string.punctuation)</em></p>
<li>Some tweets contain URL’s (eg: https:\/\/t.co\/8wl9wrT), hashtags(starting with #,@) and prefix like “RT @ManUtd:”, which should be ignored while calculating the sentiment score. For this purpose python’s  regular expression library(import re) is used</li>
</ul>

<strong>Reducer</strong>
<ul>
<li>The output is a list of <term, df, a list of <tweet_no,tf>> for each term in one line.  For example,
<p>["a", 4, [[1, 1], [2, 3], [3, 1], [4, 2]]] # This shows that term “a” has df 4 and occurs in tweets 1, 2, 3, 4 with tf 1, 3, 1, 2 respectively.</p>
<p>["all", 1, [[3, 1]]] # This shows that term “all” has df 1 and occurs in tweet 3 with tf 1.</p></li>
</ul>

<h3> Derive location of each tweet</h3>
<ul>
<li>Read the input file – nayak_nandan_tweet_data.txt</li>
<li>Read each tweet, if it has location enabled, perform the data processing as done before and then record the location against each presidential candidate and the no. of tweets from that location</li>
<li>From the total tweets, calculate the fraction of tweets commented on each presidential candidate</li>
<li>Display the results on the comment share</li>
</ul>

<h3>Final Result on ArcMap</h3>
<img src="https://github.com/NandanNayak/US-Presidential-election-prediction-from-Twitter-sentiments-using-MapReduce-framework-and-ArcMap/blob/master/ResultOnArcMap.png" />
