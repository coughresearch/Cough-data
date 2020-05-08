# /usr/bin/python
#install pandas and GetOldTweets3 library

#NOTE MAC Users can get http invalid SSL issue please install certificates.py file


import pandas as pd
import GetOldTweets3 as got


def text_query_to_csv(text_query, count):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                               .setSince("2020-04-20")\
                                               .setNear("Delhi, India")\
                                               .setMaxTweets(count)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

   # Creating list of chosen tweet data
    text_tweets = [[tweet.username,tweet.date, tweet.text,tweet.mentions,tweet.retweets] for tweet in tweets]
    # Creation of dataframe from tweets
    tweets_df = pd.DataFrame(text_tweets, columns = ['Username','Datetime', 'Text','Mentions','Retweets'])
    # Converting tweets dataframe to csv file
    tweets_df.to_csv('{}-{}tweets.csv'.format(text_query, int(count)), sep=',')
    return;

text_query = ['#coronavirus','#covid','#covidpositive','#coronapositive','#covid19']
for i in range(0,len(text_query)):
    text_query_to_csv(text_query[i], 10)
print ("Finished Generating Data")
