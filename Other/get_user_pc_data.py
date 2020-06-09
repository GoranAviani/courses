import json
import socket
import getpass
from urllib.request import urlopen

# get the username of machine
username = getpass.getuser()
print("\nUSERNAME   :   ", username)

# get the hostname of machine
hostname = socket.gethostname()
print("\nHOSTNAME   :   ", hostname)

# get the ip address of machine
machineIP = socket.gethostbyname(hostname)
print("\nIP ADDRESS :  ", machineIP)
print("########################")
# get the public ip address and the location
# open the url and store the responce
url = 'http://ipinfo.io/json'
response = urlopen(url)
# Converting JSON encoded response into Python objects
data = json.load(response)
# Fetching and displaying necessary data
print("\nPUBLIC IP :   ", data['ip'])
print("\nCITY:         ", data['city'])
print("\nSTATE :       ", data['region'])
print("\nCOUNTRY :     ", data['country'])
