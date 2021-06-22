import os
import discord
import random
from replit import db
from SpaceTradersSDK.SpaceTradersSDK1 import User

client = discord.Client()
TOKEN = os.getenv('discotoken')
discorddeveloperportalLink = os.getenv('discorddeveloperportal')  # for meta


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


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
    if message.channel.name == 'updates':  # random channel name in the discord server I've currently got this set bot set in
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'Gizmotronn':
            await message
        elif user_message.startswith('$login')
            await message.channel.sent(f'Attempting to login, {username}!')
            


# Main Function
client.run(TOKEN)
