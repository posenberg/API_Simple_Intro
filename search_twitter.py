import tweepy

#Fill in your keys, secrets, and tokens from your app created on  https://apps.twitter.com/
consumer_key = '12345678901234567890'
consumer_secret = '1234567890123456789012345678901234567890'
access_token = '1234567890123456789012345678901234567890'
access_token_secret = '1234567890123456789012345678901234567890'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#You can play with different operators using this reference:
# https://dev.twitter.com/docs/using-search
results = api.search(q="hate -RT", count=50, result_type = "recent", geocode = '37.3309913,-122.0410974,10mi' )

i = 1
for result in results:
	print "%d. %s" % (i , result.text)
    	i = i + 1

