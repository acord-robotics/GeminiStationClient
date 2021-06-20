#!/usr/bin/python
# -*- coding: utf-8 -*-

#username: Gizmotronn
#token: 097a72d9-1321-4048-9f74-b189c2c4ca00

#ship id: ckpyxboir79280715s6qs87m5un

#username: Gizmotronn
#token: 097a72d9-1321-4048-9f74-b189c2c4ca00

#Imports
import requests
import json
#------------------------------------------------------------------------------------------------

#Globals
URL = "https://api.spacetraders.io"
#------------------------------------------------------------------------------------------------

#Classes
class SpaceTradersClientTerminal:
    
    def __init__(self, token):
        self.token = token  #Bearer + token
        self.accountStatus()

    def accountStatus(self):
        print("Loading account status...")
        r = requests.get("%s/my/account" % URL, headers={'Authorization': self.token})
        content = json.loads(r.content.decode())
        self.username = content["user"]["username"]
        print("Here is your account status, " + self.username)
        content = json.loads(r.content.decode())
        print(content["user"])

    def browseLoans(self):
        print("Loading available loans...")
        r = requests.get("%s/types/loans" % URL, headers={'Authorization': self.token})
        print("Here are all available loans for you to take, " + self.username)
        content = json.loads(r.content.decode())
        print(content["loans"])

    def takeLoan(self, type):
        loanType = type
        parameters = {"type": loanType}
        print("")

        print("Processing loan...")
        r = requests.get("%s/my/loans" % URL, headers={'Authorization': self.token}, params=parameters)
        
        while (r.status_code == 422):
            print("Loan type invalid, please insert a valid loan type: ")
            loanType = input("")
            parameters = {"type": loanType}
            print("")

            print("Processing loan...")
            r = requests.get("%s/my/loans" % URL, headers={'Authorization': self.token}, params=parameters)

        print("Loan sucessfully taken, here is the corresponding info:")
        content = json.loads(r.content.decode())
        print(content)

    def browseShips(self, system):
        print("Loading ship listings in " + system)
        r = requests.get("%s/systems/%s/ship-listings" % (URL, system), headers={'Authorization': self.token})
        print("Here are all ships available for purchase, self.username")
        content = json.loads(r.content.decode())
        for ship in content["shipListings"]:
            print(ship)

    def buyShip(self, location, type):
        parameters = {"location": location, "type": type}
        print("Processing purchase...")
        r = requests.get("%s/my/ships" % URL, headers={'Authorization': self.token}, params=parameters)

        if (r.status_code == 422):
            print("Invalid purchase, please verify location and type of ship and try again")
            print("")
        else:
            print("Purchase successfull, " + self.username)
            content = json.loads(r.content.decode())
            print(content)

    def purchaseOrder(self, shipID, goodID, quantity):
        parameters = {"shipId": shipID, "good": goodID, "quantity":quantity}
        print("Placing purchase order...")
        r = requests.get("%s/my/purchase-orders" % URL, headers={'Authorization': self.token}, params=parameters)

        if (r.status_code == 422):
            print("Invalid purchase order, please verify shipID, good and quantity and try again")
            print("")
        else:
            print("Purchase successfull, " + self.username)
            content = json.loads(r.content.decode())
            print(content)


#------------------------------------------------------------------------------------------------

#Main code
print("Booting SpaceTraders client terminal...")
r = requests.get('%s/game/status' % URL)
content = json.loads(r.content.decode())
print(content["status"])

print("Are you a registered member of the SpaceTraders? Y/N")
registered = input("")
print("")

if registered == "N":
    print("Commencing account creation protocol...")
    print("What would you like to be called?")
    username = input("")
    print("")

    print("Welcome to the SpaceTraders, %s!" % username)
    print("")

    print("Requesting acess token from mainframe...")
    r = requests.post("%s/users/%s/claim" % (URL, username))

    while (r.status_code == 409):
        print("That name has been claimed, please insert a different one")
        username = input("")
        print("")

        print("Requesting acess token from mainframe...")
        r = requests.post("%s/users/%s/claim" % (URL, username))

    content = json.loads(r.content.decode())
    token = "Bearer " + content["token"]
    print("%s, your standard issue token is: %s" % (username, token))
    print("Please save this token in a safe external memory device, as losing it means termination of access to your account")
    print("")
else: #Y
    print("Commencing user validation protocol...")
    print("Please insert your access token")
    token = "Bearer " + input("")
    print("")

    print("Validating...")
    r = requests.get("%s/my/account" % URL, headers={'Authorization': token})

    while (r.status_code == 401):
        print("Invalid token please refrain from inserting \"Bearer\" before the token as it is not necessary")
        print("Please insert a valid access token")
        token = "Bearer " + input("")
        print("")

        print("Validating...")
        r = requests.get("%s/my/account" % URL, headers={'Authorization': token})

    print("Access granted!")

terminal = SpaceTradersClientTerminal(token)

print("Insert your command: (EXIT to shutdown terminal and HELP for help)")
command = input("").split()
print("")

while (command != "EXIT"):
    if (command == "HELP"):
        print("I regret to inform that this terminal does not have a helpdesk module installed")
    elif (command == ["BROWSE", "LOANS"]): 
        terminal.browseLoans()
    elif (command[:1] == ["TAKE", "LOAN"]):         #TAKE LOAN $TYPE
        terminal.takeLoan(command[2])
    elif (command[:1] == ["BROWSE", "SHIPS"]):      #BROWSE SHIPS $SYSTEM
        terminal.browseShips(command[2])
    elif (command[:1] == ["BUY", "SHIP"]):          #BUY SHIP $LOCATION $TYPE
        terminal.buyShip(command[2], command[3])
    elif (command[:1] == ["PURCHASE"]):             #PURCHASE $SHIPID $GOODID $QUANTITY
        terminal.purchaseOrder(command[2], command[3], command[4])

    print("Insert your command: (EXIT to shutdown terminal and HELP for help)")
    command = input("").split()
    print("")
#------------------------------------------------------------------------------------------------
