import keys
import tweepy as t

auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify= True)

user = api.get_user("prattprattpratt")

print(user.name) #username

print(user.description) #bio

print(user.status.text) #latest tweet

print(user.followers_count) #followers count

print(user.geo_enabled) #locate T/F

me = api.me

#print(me)

followers = []

#print(user)

cursor = t.Cursor(api.followers, screen_name = "prattprattpratt") #take all followers and save in cursor object

for account in cursor.items(10):
    followers.append(account.screen_name)

print(followers)

friends = []

cursor = t.Cursor(api.friends, screen_name = "prattprattpratt")

for friend in cursor.items(10):
    friends.append(friend.screen_name)

print(friends)

#get a users recent tweets

chris_tweets = api.user_timeline(screen_name = 'prattprattpratt', count = 5)

for tweet in chris_tweets:
    print(f"{tweet.user.screen_name}:{tweet.text}\n")

mytweets = api.home_timeline()

for tweet in mytweets:
    print(f"{tweet.user.screen_name}:{tweet.text}\n")

