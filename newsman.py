import requests
import json
import os

class User():
  # Class Attributes

  # Instance Attributes
  def __init__(self, username, token):
        self.username = username
        self.token = token

def LoginUser():
  uN = input("What is your username? ")
  t = input("What is your token? ")

  Account = User(uN, t)

  print("You are logged in as " + Account.username)


LoginUser()