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
# get the public ip address and the location

