import tweepy
#Fill in your keys, secrets, and tokens from your app created on  https://apps.twitter.com/

def post_to_twitter():

	consumer_key = '0MWtZ70TKubJqhXMYWfDtn1pc'
	consumer_secret = 'AJTBAC79DAoCLA36Zfm32HT6UxnmfayMoBuKsF8qRzOcay2P4D'
	access_token = '787933-5epwLWlO9ACbGiB9RkRdjlGlX9BoTCJbnFPAyYtOppa'
	access_token_secret = '6SEOlHBTfhqmVKEtQ6VpCmZplUUr3G9gBbf21yFmnjSCf'


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	api.update_status('Nevermind. I know now.')

