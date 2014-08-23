import tweepy

import csv


def monitor():

	#Fill in your keys, secrets, and tokens from your app created on  https://apps.twitter.com/
	consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	#You can play with different operators using this reference:
	# https://dev.twitter.com/docs/using-search

	new_tweets = api.user_timeline( 
                    screen_name="buzzfeed", 
                    count=10,
                    exclude_replies=True,
                    include_rts=False)
	
	#Create a csv file that stores your time_line search results.
	#Change "new_file.csv" if you want to save with differenting file name.
	csvFile = open('new_file.csv', 'w')
	csvWriter = csv.writer(csvFile)
	for tweet in new_tweets:
		csvWriter.writerow([tweet.text.encode('utf-8')])
		print tweet.created_at, ' ',tweet.text.encode('utf-8')
	csvFile.close()
	
monitor()
