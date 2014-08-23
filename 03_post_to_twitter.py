import tweepy

#Make sure to Enable READ-WRITE abilities on your application on your Twitter developer account. 

def post_to_twitter():
	#Fill in your keys, secrets, and tokens from your app created on  https://apps.twitter.com/
	consumer_key = 'xxxxxxxxxxxxxxxxxxxx'
	consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	api.update_status('I am having a good day.')

