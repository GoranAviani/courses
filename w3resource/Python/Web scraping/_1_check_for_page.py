#1. Write a Python program to test if a given page is found or not on the server.

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


while True:
    userURL = input("enter a webpage without a https://: or x to E[x]it!: ")

    if userURL.lower() == "x":
        print("Good bye")
        break
    else:
        try:
            html = urlopen("https://" + userURL)
        except HTTPError as e:
            print("HTTP error")
        except URLError as e:
            print("Page not found")
        else:
            print("HTMP page: \n\n----------------------------------------------------------------------------\n\n")
            print(html.read())