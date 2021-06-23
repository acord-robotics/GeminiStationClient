# Temporarily removing folder SpaceTradersSDK to simplify the structure
#from SpacePyTraders import client
import requests
import json
import os
import time

URL = "https://api.spacetraders.io"

class User():

  # Instance Attributes
  def __init__(self, username, token):
        self.username = username
        self.token = token

  def LoginUser():
    USERNAME = input("What is your username? ")
    TOKEN = input("What is your token? ")

    Account = User(USERNAME, TOKEN)

    print("You are logged in as " + Account.username)

    api = client.Api(Account.username,Account.token)

    print(api.users.get_your_info())