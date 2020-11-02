import keys
import tweepy as t
import json
#from wordcloud import WordCloud

auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify= True)
'''1
#Print out screen name of the users and the text of the tweet
tweets = api.search(q="Vote", count = 3)
#print(tweets)

for tweet in tweets:
    print(f"{tweet.user.screen_name}:{tweet.text}\n")

tweets = api.search(q = 'collegefootball', count = 2)    
    
for tweet in tweets:
    print(f"{tweet.user.screen_name}:{tweet.text}")
'''
'''2
#places with trending topics
#returns list of dictionaries

trends_available = api.trends_available()

print(len(trends_available))
print(trends_available[:3])
'''

'''3
world_trends = api.trends_place(id = 1) #this id is the world trend
#print(world_trends)

outfile = open('world_trends.json','w')
json.dump(world_trends, outfile, indent = 5)

trends_list = world_trends[0]['trends']
#print(trends_list)

#grab tweets that are above 10,000 or not null
trends_list = [t for t in trends_list if t['tweet_volume']] #with the if tweet volume its checking if its false or not
#print(trends_list)

from operator import itemgetter

trends_list.sort(key = itemgetter('tweet_volume'), reverse = True) #specifies key to which to sort
#print(trends_list[:5])

for names in trends_list[:5]:
    print(names['name'])
'''

#trending topics in new york city, and create word cloud

from wordcloud import WordCloud
from operator import itemgetter
nyc_trends = api.trends_place(id = 2459115)
outfile = open('nyc_trends.json', 'w')
json.dump(nyc_trends, outfile, indent = 3)

nyc_trending = nyc_trends[0]['trends']
#print(nyc_trending)

nyc_trending = [t for t in nyc_trending if t['tweet_volume']] 

nyc_trending.sort(key = itemgetter('tweet_volume'), reverse = True)

topics = {}

#add name and tweet volume, name as key and volume as value to the key in dictionary
for trend in nyc_trending:
    topics[trend['name']] = trend['tweet_volume']

#print(topics)

wordcloud = WordCloud(
    width = 1600, height = 900,
    prefer_horizontal = 0.5, min_font_size = 10,
    colormap = 'prism', background_color = 'white'
)

wordcloud = wordcloud.fit_words(topics)
wordcloud = wordcloud.to_file("TrendingTwitter_fall2020.png")