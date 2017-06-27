#!/usr/bin/python3

#tweepy is the main library for our bot
import tweepy
from forest_keys import *

#set up oauth
#never actually store your keys and secrets on github!
auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

#send a basic tweet to my pal Neeraj
api.update_status('Sending secret-robo-forest vibes to @Neeraj_K0')
