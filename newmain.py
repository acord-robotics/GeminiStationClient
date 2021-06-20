from SpacePyTraders import client
import requests
import json
import os
import time

URL = "https://api.spacetraders.io"

class User():
  # Class Attributes

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

# Functions
#def Loans():
  #client.Loans(Account.username, Account.token)

#def Command():
 # command1 = input("What command would you like to use? Type 'help' to view all available commands. ")

# Main Function

User.LoginUser()
time.sleep(3)

#loansAvailable = requests.get(URL + "/types/loans" headers={'Authorization': 'token Accoount.token'})
#print(loansAvailable)

#Command()
#command1 = input("What command would you like to use? Type 'help' to view all available commands. ")
#if command1 == "help" or "HELP":
  #print("HELP/help = View all commands")
  #time.sleep(1)
 # print("Loans = View available loans")
#if command1 == "Loans" or "LOANS" or "loans":
  #Loans()