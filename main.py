import os
import discord
from time import sleep
import asyncio
import tweepy


#This is your discord bot token DO NOT SHARE!!
discord_token = os.environ['discord_token']

#Here is where we will store information for our twitter developer api keys
#this will be twitter bot 1
access_token_secret1 = os.environ['access_token_secret']
access_token1 = os.environ['access_token']
consumer_secret1 = os.environ['consumer_secret']
consumer_key1 = os.environ['consumer_key']

#Here is where we will store information for our twitter developer api keys
#this will be twitter bot 2
access_token_secret2 = os.environ['access_token_secret']
access_token2 = os.environ['access_token']
consumer_secret2 = os.environ['consumer_secret']
consumer_key2 = os.environ['consumer_key']

#Here is where we will store information for our twitter developer api keys
#this will be twitter bot 3
access_token_secret3 = os.environ['access_token_secret']
access_token3 = os.environ['access_token']
consumer_secret3 = os.environ['consumer_secret']
consumer_key3 = os.environ['consumer_key']

#This is where we we auth twitter api keys via tweepy
auth=tweepy.OAuthHandler(consumer_key1,consumer_secret1)
auth.set_access_token(access_token1,access_token_secret1)
api = tweepy.API(auth)

client=discord.Client()

#here are your channels ids for each bot
discord_channel_id1='ENTER CHANNEL ID1'
discord_channel_id2='ENTER CHANNEL ID2'
discord_channel_id3='ENTER CHANNEL ID3'


#This wil make sure out bot is online and ready , as well as set a activity presence
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for tweets to post"))
    print(f'{client.user} has connected to Discord!')
    sleep(0.5)
    print('Bot is ready!')


#This is the action to take
#Watch for messages and post tweet upon a message post.
@client.event
async def on_message(message):
    if message.author != client.user and str(message.channel.id) ==discord_channel_id1 :
        api.update_status(status=message.content)
        print('Tweet posted from channel 1')
    
    if message.author != client.user and str(message.channel.id) ==discord_channel_id2 :
        api.update_status(status=message.content)
        print('Tweet posted from channel 2')
    
    if message.author != client.user and str(message.channel.id) ==discord_channel_id3 :
        api.update_status(status=message.content)
        print('Tweet posted from channel 3')
    



async def main_func():
    await client.start(discord_token)


asyncio.get_event_loop().run_until_complete(main_func())
