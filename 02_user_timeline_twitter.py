import tweepy
import csv
#Fill in your keys, secrets, and tokens from your app created on  https://apps.twitter.com/

def monitor():



	consumer_key = '538LEWAOqt8hAMgTdfqoY2J1b'
	consumer_secret = 'xbSsONrS2mBhRn5ucU5XkKs6Mr4AK9FNKTsi07bDr4JJuEqHO5'
	access_token = '787933-ZQ0ljPUD2hja9ENwHqmH63nmqwHYXfMWWujkBAonNiu'
	access_token_secret = 'SfSeONIcOJ7DBuyOsoU5fN3NQTPqCYktC1bdwHWoLztR5'


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

	csvFile = open('result.csv', 'w')
	csvWriter = csv.writer(csvFile)

	'''for tweet in new_tweets:
		csvWriter.writerow(list(tweet.text.encode('utf-8')))
		print i,' ', tweet.text.encode('utf-8')
		print tweet.created_at
		i=i+1'''

	i=0
	for tweet in new_tweets:
		csvWriter.writerow([tweet.text.encode('utf-8')])
		print tweet.created_at, ' ',tweet.text.encode('utf-8')

	csvFile.close()
monitor()