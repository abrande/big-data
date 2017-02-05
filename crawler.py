from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

# This class defines MyListener class - an object of which essentially
# keeps the connection going and keep pulling new tweets from Twitter server.
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('output.txt', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# Consumer/Access key/secret/token obtained from Twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# The following two lines create an authorization object with your above authentication info.
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# This line finally calls Twitter's Streaming API.
twitter_stream = Stream(auth, MyListener())

# Here, we define our query terms - inside a list.
# For example, below, we crawl all tweets mentioning #donaldtrump.
# For more details refer to https://dev.twitter.com/docs/streaming-apis
query_terms = ['donaldtrump','maga']
twitter_stream.filter(track=query_terms)