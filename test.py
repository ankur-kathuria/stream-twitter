import json
import oauth2 as oauth
import time

def filter_complaints(tweets):
	i=1
	for tweet in tweets:
		for hashtag in tweet['entities']['hashtags']: 
			if hashtag['text'] == 'complaint':
				print tweet['text'],'-----------',tweet['id']
				if i == 1:
					since_id=tweet['id_str']
					i=i+1
	return since_id




			# print tweet['entities']['hashtags'][0]['text']
			# print len(tweet['entities']['hashtags'][0]) 	
			# print tweet['text']
			# print tweet['id']
			# if i == 1:
			# 	since_id=tweet['id_str']
			# 	i=i+1


consumer_key = 'sQoVCJuws1MYhqQ1yrHTBIL4E'
consumer_secret = 'GzsVR3Bb8qX9D0K1P4YFk3e6nyn9MBWH7hMxX888gNW2pMFoDE'
access_token = '816227950055960576-T6N8bHAcURRHIWFgBUeXPRsprkX6BMr'
access_token_secret='bO573RZlDlAUxPx5YmNTidH6zzGulsxdw3P91aHxRXHd2'
since_id='11111'

#request_token_url = 'https://api.twitter.com/oauth/request_token'
#access_token_url = 'https://api.twitter.com/oauth/access_token'
#authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token=oauth.Token(key=access_token,secret=access_token_secret)
client = oauth.Client(consumer,access_token)

#endpoint = 'https://api.twitter.com/1.1/search/tweets.json?q=complaint&since_id=0'
#endpoint = 'https://userstream.twitter.com/1.1/user.json'
#endpoint = 'https://api.twitter.com/1.1/statuses/user_timeline.json?since_id=816305139677941760'
endpoint = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json?q=complaint'
#response,data=client.request(endpoint,method='POST',body='track="twitter"')

while True:
	
	response,data=client.request(endpoint+'&since_id='+since_id)

	#print data
	tweets=json.loads(data)
	since_id=filter_complaints(tweets)
	time.sleep(30)

