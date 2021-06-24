from account import User
import requests
import discord
import os
import time
import asyncio
from SpacePyTraders import client

DiscordBot = discord.Client()

@DiscordBot.event
async def on_message(message):
    print(message.content) # Every message sent will be printed to the console

@DiscordBot.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")

@DiscordBot.event
async def on_message(message):
    username = str(message.author).slit('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'feed':
        if user_message.startswith("!Username"):
            os.environ["Username"] = user_message.replace('!Username', '')
        if user_message.startswith("!Token"):
            os.environ["Token"] = user_message.replace('!Token', '')
            api = client.Api(os.environ["Username"],os.environ["Token"])
            await message.channel.sent(api.account.info())
            # We need to get the !Token message to be in place after the !Username message/command
            # What we've done now is allow this to integrate with SpacePyTraders
            # Tale/stories for python & web: https://github.com/irmen/Tale
            # https://github.com/VrtK/SimpleMMO-Bot/blob/main/SimpleMMO.py - so investigate Selenium Py
            # Now we need to get this working with a db (like flask/replit) and a web application 
            # Eventually separate the components from DiscordBot

""" If we were doing this in the terminal
os.environ["Username"] = input("What is your username? ")
os.environ["Token"] = input("What is your token? ")
#for k, v in os.environ.items():
    #print(f'{k}={v}')


#print(api.account.info())

#097a72d9-1321-4048-9f74-b189c2c4ca00
#8a362bd4-9f29-4b94-9eca-764e18b74b53"""