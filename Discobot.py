import discord
import os
import time
import asyncio
import requests
from account import User

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content) # Now every message sent will be printed to the console

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi

def jls_extract_def():
    
    return 


@client.event
async def on_message(message):
    username = str(message.author).split('#')[
        0]  # Get discord user's username without the #
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # Housekeeping
    if message.author == client.user:
        return  # Don't let the bot log its own messages

    # Message awaits
    if message.channel.name == 'feed':  # random channel name in the discord server I've currently got this set bot set in
        if user_message.startswith("!login"):
            await message.channel.send("Enter your Username, starting with !Username")
        if user_message.startswith("!Username"):
            userNameTemp = user_message.replace('!Username', '')
            message.author = User(str(userNameTemp), "Hi")
            await message.channel.send("Your username is: " + userNameTemp + ", now enter your token starting with !Token")
        if user_message.startswith("!Token"):
            userTokenTemp = user_message.replace('!token ', '')
            User[0].token = str(userTokenTemp)
            await message.channel.send("Hi" + User[0])
        

client.run("ODU2MDkwNjM2MDE2NTQ5ODg4.YM7-iQ.YOaIjnVh8bcdg8WITVBbO0K9zNY")
# 097a72d9-1321-4048-9f74-b189c2c4ca00