import tweepy

#Fill in your keys, secrets, and tokens from 
#your app created on  https://apps.twitter.com/

def run():
	consumer_key = 'xxxxxxxxxxxxxxxxxxx'
	consumer_secret = 'xxxxxxxxxxxxxxxxxxx'
	access_token = 'xxxxxxxxxxxxxxxxxxx'
	access_token_secret = 'xxxxxxxxxxxxxxxxxxx'


	auth = tweepy.OAuthHandler(
		consumer_key, 
		consumer_secret)

	auth.set_access_token(
		access_token, 
		access_token_secret)

	api = tweepy.API(auth)

	#You can play with different operators using this reference:
	# https://dev.twitter.com/docs/using-search
	results = api.search(
		q="happy -RT -Birthday -ur", 
		count=50, 
		result_type = "recent", 
		geocode = '37.3309913,-122.0410974,10mi' )

	i = 1

	for result in results:
		print "%s %s" % (i, result.text.encode('utf-8'))
		i = i + 1

run()
